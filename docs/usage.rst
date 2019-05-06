=====
Usage
=====

To use pysank in a project

- To create directory

::

    from pysank.pysank import *
    from pysank import pysank as ps
    import pysank.pysank as ps2

    dirname = 'data_input'
    dir_out = 'data_output'

    ps.create_directory(dirname)
    ps2.create_directory(dir_out)
    create_directory(dirname)

- To check if it's a git repository

::
    print("Is it a git repo?: Ans:{}".format(is_it_git_repo()))

- To get the branch name

::
    print("get git branch name: {}".format(get_git_branch_name()))

- To get the python filename in execution

::
    print("get file name: {}".format(get_running_filename()))

- To get the git revision number -- Full

::
    print("get git revision hash: {}".format(get_git_revision_hash()))

- To get the git revision number -- Short

::
    print("get git revision hash short: {}".format(get_git_revision_short_hash()))
