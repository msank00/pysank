=====
Usage
=====

To use pysank in a project

- To create directory

::

    from pysank import smutil as sm

    dirname = 'data_input'
    dir_out = 'data_output'

    sm.create_directory(dirname)
    sm.create_directory(dir_out)
    sm.create_directory(dirname)


- To check if it's a git repository

::

    print("Is it a git repo?: Ans:{}".format(sm.is_it_git_repo()))

- To get the branch name

::

    print("get git branch name: {}".format(sm.get_git_branch_name()))

- To get the python filename in execution

::

    print("get file name: {}".format(sm.get_running_filename()))

- To get the git revision number -- Full

::
    
    print("get git revision hash: {}".format(sm.get_git_revision_hash()))

- To get the git revision number -- Short

::
    
    print("get git revision hash short: {}".format(sm.get_git_revision_short_hash()))
