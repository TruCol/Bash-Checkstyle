# Checkstyle for bash
WIP: CI tool to verify some degree of Google Shell Style Guide compliance.

[Shellcheck](https://github.com/koalaman/shellcheck) provides wonderful checks on compliance of bash code to some standard. I think it would be awesome if we can extend the segments of Bash code that are covered by some kind of automated coding style checker to the complete bash scripts, including comments/documentation. I believe some parts of the [Shell Style Guide](https://google.github.io/styleguide/shellguide.html) by Google can be verified automatically.

## Example
Looking at the [function comments](https://google.github.io/styleguide/shellguide.html) elements, it states: `All function comments should describe the intended API behaviour using:`

0. Description of the function. - The content of this description is currently not deterministically verifiable, and I have not yet found a practical NLP/AI solution. However, 
    - [ ] a checker can verify whether at least whether some description is presented in the function comments. 
    - [ ] the open source segment of LanguageTools can be used to verify whether this description is gramatically correct (whilst allowing for misspellings/unrecognised words).  
2. Globals: List of global variables used and modified. - I think/assume one could use static code analysis to determine which variables in a function are local, and which are global. If this assumption is valid, then: 
    - [ ] the checkstyle can verify whether these global variables are indeed contained in the function comments. 
    - [ ] Vice versa, the checkstyle can verify the globals specified in the function comments are indeed used in the function. 
    - [ ] If a root directory is passed into the checkstyle, it could also scan all bash files to determine whether the globals of each function, are defined somewhere in the code.
3. Arguments: Arguments taken. - 
    - [ ] The checkstyle could verify all incoming arguments are included in the function comments. 
    - [ ] Vice versa, checkstyle could verify all arguments specified in the function comments, are included in the function.
4. Outputs: Output to STDOUT or STDERR. - I do not yet have a lot of experience with this, however I assume that one could include a code style assumption, stating all echo's should go to channel `x` and all errors should go to channel `Y`. If that assumption is valid, then  I think 
    - [ ] checkstyle could verify whether all `echo something` are indeed redirected to that channel using `>2 something`.
5. Returns: Returned values other than the default exit status of the last command run. - 
    - [ ] The checkstyle could verify all `return` statements are included in the function comments. 
    - [ ] Vice versa, checkstyle could verify all return statements specified in the function comments, are included in the function.

Just for convenience, below is a function to see how checkstyle may run on it:
```
#######################################
# Returns the architecture of the machine on which this service is ran.
# The code that detects the architecture on the device returns something
# diffent (x86_64) than the identifier that GitLab uses to indicate which 
# architecture is used (amd64). That is why the detected architecture is 
# mapped.
# Source: https://askubuntu.com/questions/189640/how-to-find-architecture-of-my-pc-and-ubuntu
# Local variables:
#  architecture
#  mapped_architecture
# Globals:
#  None.
# Arguments:
#  The detected architecture of the device on which this code is running.
# Returns:
#  0 if funciton was evaluated succesfull.
#  14 if the code is ran on an architecture that is not (yet) supported.
# Outputs:
#  A string that represents the architecture on which this code is running.  
#######################################
get_architecture() {
	local architecture
	architecture=$(uname -m)
	
	# Parse architecture to what is available for GitLab Runner
	if [ "$architecture" == "x86_64" ]; then
		local mapped_architecture=amd64
	else
		error "ERROR, did not yet find GitLab installation package and GitLab runner installation package for this architecture:$architecture"
		exit 14
	fi
	
	echo $mapped_architecture
}
```

## Project values
I think it is important to facilitate user freedom, I think this could be manifested by taking the following requirements in mind in the development process:
 - [ ] even though this project may start out with the "Google Style Guide for Bash", other style guides should be supported as well. 
 - [ ] Users should be able to (easily) turn checks on and off.
 - [ ] Users should be able to (easily) swap out checks in a certain topic, for example in the topic of `function comments` style guide `a` might suggest option `1`, whereas style guide `b` might propose option `2`. It would be nice if people can choose style guide `a` and still opt for option 2 in the topic of `function comments`. (As long as the options are not conflicting).

## Project Approach
I think it could be valuable to perform the following steps:

0. Identify which elements from the Google Style Guide for Bash can be verified automatically.
1. Clearly state which opinions/assumptions are required to ensure some style guide elements can be verified automatically.
2. That list of automatically verifiable style guide elements should be crosschecked with Shellcheck to prevent re-doing the work that that project already did. 
3. The remaining list of automatically verifiable style guide elements should be implemented. 

## Implementation
My personal preference for implementing this checkstyle for Bash, would be Python, for the following two reasons:

0. I believe it is easiest for most other people to contribute to.
1. I think it is a user-friendly language with relatively easy to use text parsing possibilities.
