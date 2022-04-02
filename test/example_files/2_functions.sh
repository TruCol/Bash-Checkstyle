#!/bin/bash
# A file that contains functions to make modifications to GitLab
# repositories.

#######################################
# 
# Local variables:
# 
# Globals:
#  None.
# Arguments:
#   
# Returns:
#  0 if 
#  7 if 
# Outputs:
#  None.
# TODO(a-t-0): change root with Global variable.
#######################################
# Structure:Configuration
# Returns the GitLab installation package name that matches the architecture of the device 
# on which it is installed. Not every package/GitLab source repository works on each computer/architecture.
# Currently working GitLab installation packages have only been found for the amd64 architecture and 
# the RaspberryPi 4b architectures have been verified.
get_gitlab_package() {
	architecture=$(dpkg --print-architecture)
	if [ "$architecture" == "amd64" ]; then
		echo "$GITLAB_DEFAULT_PACKAGE"
	elif [ "$architecture" == "armhf" ]; then
		echo "$GITLAB_RASPBERRY_PACKAGE"
	fi
}

#######################################
# Deletes the repository if it doesn't exist in the GitLab server.
# Local variables:
#  deleted_repo_is_found
#  gitlab_repo_name
# Globals:
#  None.
# Arguments:
#   Name of the GitLab repository.
# Returns:
#  0 if funciton was evaluated succesfull.
#  7 if the repository was not found.
# Outputs:
#  None.
# TODO(a-t-0): change root with Global variable.
#######################################
delete_gitlab_repo_if_it_exists() {
  local gitlab_repo_name="$1"

  if [ "$(gitlab_mirror_repo_exists_in_gitlab "$gitlab_repo_name")" == "NOTFOUND" ]; then
    assert_equal "$(gitlab_mirror_repo_exists_in_gitlab "$gitlab_repo_name")" "NOTFOUND"
  elif [ "$(gitlab_mirror_repo_exists_in_gitlab "$gitlab_repo_name")" == "FOUND" ]; then
    # TODO(a-t-0): change root with Global variable.
    delete_existing_repository "$gitlab_repo_name" "root"
    sleep 5
    local deleted_repo_is_found
	deleted_repo_is_found="$(gitlab_mirror_repo_exists_in_gitlab "$gitlab_repo_name")"
    assert_equal "$deleted_repo_is_found" "NOTFOUND"
  else
    echo "The repository was not NOTFOUND, nor was it FOUND. "
    exit 7
  fi
}