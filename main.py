# USE GIT BASH IN TERMINAL

#####################################################
############### COMMANDS ############################

# pwd: returns current directory path

# ls: returns current directory (add -a to show hidden files)

# cd ..: go up one directory

# cd <path>: go to path directory

# cd <dir>: go to sub directory <dir> (PRESS TAB AS TYPING DIR TO AUTOFILL)

# mkdir <name>: create a directory called <name>

# touch <file.ext>: create file with extension in current directory

# code <file.ext>: create file and open/open in vscode unsaved
# NOTE: code always opens the file with vscode
# to open with pycharm use the following (SPECIAL NOTE: PYCHARM MUST BE IN YOUR SYSTEM PATH!!)
# pycharm64 <file.ext>

# clear: clear the terminal

################################################################################
###################### GIT COMMANDS (LOCAL REPOSITORY) #########################

##### git init: initialises an empty Git repository inside the current directory (CALLED THE WORKING DIRECTORY)
# the repository is located in a hidden dir called .git in the current dir
# we can see hidden files using command: ls -a
# the repository will track changes, commit changes, and perform version control

# to track changes to a file using git it needs to be added to the STAGING AREA
#### git status: use to see that status of files in working directory (show what ones are in staging area)

#### git add <file.ext>: use to add a file from the working directory to the staging area
#### git add .: use to add ALL files inside the working directory
#### git rm --cached <file.ext>: remove a file from the staging area
#### git rm --cached -r .: remove ALL files from the staging area

#### git commit -m "description message": use to commit a files in staging area. use -m to add a description message to the commit
# this commits the changes to the git repository
# the message is very important as it acts as a label for what changes are made in that commit
# this message will be shown in the terminal when using git log, and also in github
# GENERAL PRACTICE IS TO WRITE THE MESSAGE IN PRESENT TENSE. ("complete chapter 1", rather than "completed chapter 1")

#### git log: use to see what commits you have made
# each commit will be represented by a hash, with details including the message passed when committed
# the commit with HEAD after the hash is the current state of the branch you are on
# the HEAD will follow with all branches and repositories that it is the current state on

# WHEN ANY CHANGES ARE MADE TO FILES IN THE WORKING DIRECTORY THEY WILL SHOW IN GIT STATUS AS FILES THAT HAVE CHANGES
# THAT HAVE NOT BEEN COMMITTED TO THE REPOSITORY

#### git diff <file.ext>: show changes between the current version of the file and the last committed version
# lines in green are new additions to the file
# lines in red have been removed from the file

#### git checkout <file.ext>: revert back to the last commited version of the file from the repository
#  THE FILE MUST BE IN THE STAGING AREA

###############################################################################
######################## GITHUB REMOTE REPOSITORY #############################

#### PUSH EXISTING LOCAL REPOSITORY COMMITS OVER TO THE REMOTE REPOSITORY ####

#### git remote add <name> <url>: create the remote repository
# <URL> IS THE URL OF THE GITHUB REPOSITORY
# KEEP <NAME> AS 'origin'!! THIS IS COMMON PRACTICE (but could be something else)

#### git branch -M main: RUN THIS COMMAND BEFORE EXECUTING PUSH
# THIS JUST NEEDS TO BE DONE BEFORE THE FIRST PUSH

#### git push -u <remote name> <branch name>
# push commits from local repository over to remote repository using the -u flag (links the repositories)
# push towards the remote repository named origin
# push to the branch called main (main is the default branch/main branch of your commits)
# the main branch is like a timeline of sequential commits
# the push command pushed the main branch over to the remote repository on github
# THIS COMMAND CAN TAKE A VARIED AMOUNT OF TIME TO EXECUTE AS IT HAS TO UPLOAD THE FILES DEPENDING ON THE SIZE

##############################################################################

#### USING IGNORE TO PREVENT CERTAIN FILES FROM BEING COMMITTED TO LOCAL AND REMOTE REPOSITORIES #####
# some files that contain secrets like api keys and passwords.
# also files that contain your operating system data (.DS_Store for example)

#### touch .gitignore: create the hidden .gitignore file that will contain the files we want to ignore when committing
#### code .gitignore: open the file in vscode so that we can list the files
# each line in the file represents an ignore rule

# https://github.com/github/gitignore/blob/main/Python.gitignore has a great template for python projects
# to copy and paste into the .gitignore file

##############################################################################

#### CLONING A REMOTE REPOSITORY, PULLING IT TO A LOCAL REPOSITORY ####
# cloning a remote repository allows you to have your own copy, doing whatever you like to it

#### git clone <url>: clone the remote repository (saved into current dir as a new dir with its name)

# you can then load the project as your own

##############################################################################

#### BRANCHING AND MERGING ####

#### git branch <name of branch>: create a new branch with the set name using current commit

#### git branch: show a list of branches.  the branch with the * is the current branch you are on

#### git checkout <name of branch>: switch to the chosen branch
# FILES WILL BE AUTOMATICALLY CHANGED WHEN CHANGING TO A DIFFERENT BRANCH
# THIS INCLUDES FILES THAT DON'T EXIST INSIDE THE DIRECTORY AS WELL!

#### git checkout -b <name of branch>: create a branch and checkout to it at the same time

#### git merge <name of branch>: merge chosen branch with the current branch you are on

##############################################################################

#### FORKING AND PULL REQUESTS ####

# forking takes a copy of a repository and places it under your own github account
# different to cloning, that saves to your local repository

# when you fork a repository you now own that fork, and can do whatever you like with that copy
# you can then clone that copy to work on it within your local repository
# after finishing work within your local repository, you can push it back to your remote repository

# IF YOU WANT THE ORIGINAL OWNER TO INCORPORATE YOUR CHANGES YOU MUST DO A PULL REQUEST!!

# only collaborators have write access to the original repository without a pull request!