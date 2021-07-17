# Website_Deploy

This is the deployment of a static website using Python with flask.

## Create Virtual environment

Note - pyenv is used to manage python versions

link for details are here <https://realpython.com/pipenv-guide/>

```{.sh}
# set the version of python needed to deploy onto the hosted service using "pyenv"
$ pyenv versions ## list all the versions of python available in pyenv
$ pyenv local 3.8.10 # this will set the python version for the current folder
# Create a virtual environment using pipenv - this uses a pipfile rather than a requirements.txt // venv uses a requirements.txt
$ pipenv --python3.8.10
# Activate the pipenv
$ pipenv shell
# install the packages used
$ pipenv install flask frozen_flask
# once finished fun pipfile lock to generate the file for the dependencies
$ pipenv lock
# to exit the pipenv run exit - this will deactivate the pipenv
$ exit
```
