## Create the project stub

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

The final command puts all source in `src` and project management files in `src/project`.

Open the project in PyCharm and:

1. Create a new `.gitignore` file using the Python template.
    1. Remove the `.python-version` entry
1. Open PyCharm Preferences -> Project: be -> Project Interpreter
    1. Click the 'Settings' gear icon right of the Project Interpreter
    1. Select 'Existing environment'
    1. Select 'dgi-3.7.0'
    1. OK all dialogs
1. Commit all files as an 'initial commit'

At this point, the project is setup for editing in PyCharm and is runnable from `be/src` with `./manage.py runserver`.

## Add ReST support

```
ᐅ pip install djangorestframework
Collecting djangorestframework
  Using cached https://files.pythonhosted.org/packages/90/30/ad1148098ff0c375df2a30cc4494ed953cf7551fc1ecec30fc951c712d20/djangorestframework-3.8.2-py2.py3-none-any.whl
Installing collected packages: djangorestframework
Successfully installed djangorestframework-3.8.2
ᐅ pip freeze
Django==2.1.1
djangorestframework==3.8.2
pytz==2018.5
```

* Add `djangorestframework==3.8.2` to constraints.txt
* Add `djangorestframework` to requirements.txt

## Add Operational support

Create a `requirements-dv.txt` and add some favorites:

```
-r requirements.txt

black
coverage
ipython
pylint
pytest
```

Now, the local dev setup is `pip install -r requirements-dv.txt`

### Setup pylint

Generate a boilerplate `.pylintrc` with: `pylint --generate-rcfile > .pylintrc`

Add pylint support to PyCharm (2018.2.3):  Open PyCharm preferences, select External Tools, and click the add button.

* Name: pylint
* Description: A Python source code analyzer which looks for programming errors, helps enforcing a coding standard and sniffs for some code smells.
* Program: []output from 'pyenv which pylint']
* Arguments: $FilePath$
* Working Directory: $FileDir$
* Synchronize files after execution: checked

Now you can pylint any file or directory with a right-click and External Tools -> pylint

### Setup coverage

Add the default `.coveragerc` and tweek it a little.

### Add common scripts

* `pip-clean.sh` - remove all dependencies for testing pip install.
* `check-types.sh` - run `mypy` to check type annotations
* `format.sh` - run `black` to format all files

At this point, we have a pretty workable project stub. There is more that could be added but it is largely project specific. 

Commit code.

## Create the first app (endpoint)



## TODO

* Add a docker postgres that persists data to a local data dir
* Figure out a basic stock schema
* Define the basic stock model
* Run migrations
* Add celery
* Figure out a financial vehicle source
* Add a celery task to identify dividend yielding stocks
* Run the task to seed the database
* Figure out a schema for dividend historical data
* Create a celery task to gather that data for each stock
* Define ReST operations to present that data to fe
* Figure out how to display that data in a meaningful way - start the vue fe
* Figure out how to value dgi stocks
* Figure out how to display best values

