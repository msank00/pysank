## How to deploy your own package

- Initially set up with cookie cutter:
    - [link](https://github.com/audreyr/cookiecutter-pypackage)  
- Update code
- Update documentation
- Push code to master
    - travis `CI/CD` will start 
- Use: `bumpversion patch|minor|major`
    - This step will create the appropriate sequential tags
- Push the tags to github:  `git push --tags`
    - Travis CI/CD will start
    - Project will be released in `pypi` with the new tag

**Note:** Only a pypi release updates the documentation in readthedocs website  