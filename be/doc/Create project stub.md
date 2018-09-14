# Creating this app

In the `dgi/be` directory:

```sh
# Install pyenv, if not already installed
brew install pyenv
brew install pyenv-virtualenv

# Setup the virtual-env
pyenv install 3.7.0
pyenv virtualenv 3.7.0 dgi-3.7.0
echo dgi-3.7.0 > .python-version

# Install Django
pip install --upgrade pip
pip install Django

# Constrain Django to the version we just installed
echo "Django==2.1.1" > constraints.txt
echo "-c constraints.txt\n\nDjango" > requirements.txt

# Create the Django starter app
mkdir src
django-admin startproject project src
```

The final command puts all source in `src` and project management files in `project`.

Open the project in PyCharm and:

1. Create a new `.gitignore` file using the Python template.
    1. Remove the `.python-version` entry
1. Open PyCharm Preferences -> Project: be -> Project Interpreter
    1. Click the 'Settings' gear icon right of the Project Interpreter
    1. Select 'Existing environment'
    1. Select 'dgi-3.7.0'
    1. OK all dialogs
1. Commit all files as an 'initial commit'
