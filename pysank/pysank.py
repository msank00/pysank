# -*- coding: utf-8 -*-
"""Main module."""

import os
import subprocess
import sys
from subprocess import call, STDOUT


def create_directory(directory_name):
    """Create directory safely after checking if it already 
    exists or not.
    
    Arguments:
        directory_name {str} -- name of the directory 
    """
    if os.path.exists(directory_name):
        print("Directory: {}/ already exists.".format(directory_name))
    else:
        os.makedirs(directory_name)
        print("Directory: {}/ created.".format(directory_name))


def get_git_revision_hash():
    """Get the git revision hash - full form 
    
    Returns:
        [string] -- revision hash - full form
    """

    return subprocess.check_output(["git", "rev-parse", "HEAD"]).decode("utf8").strip()


def get_git_revision_short_hash():
    """Get the git revision hash - short form
    
    Returns:
        [string] -- get git revision hash - short form
    """
    return (
        subprocess.check_output(["git", "rev-parse", "--short", "HEAD"])
        .decode("utf8")
        .strip()
    )

def get_git_branch_name():
    """Get the current git branch name
    
    Returns:
        [string] -- git branch name
    """
    return (
        subprocess.check_output(["git", "symbolic-ref", "--short", "HEAD"])
        .decode("utf8")
        .strip()
    )  # [0:-1]


def get_running_filename():
    """Get the running python script name
    
    Returns:
        [string] -- running python script name
    """
    return os.path.basename(sys.argv[0])


def is_it_git_repo():
    """Check if the current repo is under Git
    
    Returns:
        [bool] -- True / False
    """
    if call(["git", "branch"], stderr=STDOUT, stdout=open(os.devnull, "w")) != 0:
        return False
    else:
        return True
