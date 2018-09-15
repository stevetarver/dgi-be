## Create the project stub

This section creates a boilerplate Django Rest Framework app with a dedicated virtual-env and some favorite tools and PyCharm integration - could be used for any DRF project.

At repo root:

```sh
# Install pyenv, if not already installed
brew install pyenv
brew install pyenv-virtualenv

# Install our base python version - for use with pyenv virtual-envs
pyenv install 3.7.0

# You MUST create the virtual-env specifying the python version to avoid
# 'command not found' errors when running some external tools.
pyenv virtualenv --python=python3.7 3.7.0 dgi-3.7.0

# Create .python-version which automatically activates this venv on dir entry
pyenv local dgi-3.7.0

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

## Add Operational support

Create a `requirements-dv.txt` and add some favorites:

```
-r requirements.txt

black
coverage
ipython
mypy
pre-commit
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

### Setup black

See `pyproject.toml`

### Setup pre-commit

See `.pre-commit-config.yaml` installed at repo root.

Run `pre-commit run --all-files` to test your configuration.

Run `pre-commit install` to install pre-commit into your git hooks. pre-commit will now run on every commit.

To update to the latest version of your hook repos, run `pre-commit autoupdate`.

### Add common scripts

* `pip-clean.sh` - remove all dependencies for testing pip install.
* `check-types.sh` - run `mypy` to check type annotations
* `format.sh` - run `black` to format all files


### Add DRF (ReST support)

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

**NOTE**: we are only constraining the major frameworks instead of all dependencies. We could lock this down more tightly by `pip freeze > constraints.txt` after every install. In practice, if a framework updates a dependency without changing its version, it is an important bug fix that does not break backwards compatibility. Those changes haven't bit me yet, so I err on the liberal side.

In `src/project/settings.py`:

Add to `INSTALLED_APPS`: "rest_framework"

Add DRF config:

```
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
}
```

**TODO**: Since we are only using Django for DRF, we should probably strip out all the additional functionality for templates, etc. Since our app is not performance sensitive, we will leave that as a prod tuning effort.

### Common commands

* `pip install -r requirements-dv.txt`: Install all local dev dependencies.
* `./scripts/pip-clean.sh`: Remove all python virtual-env installed dependencies to test prod/dv venv setup.
* `pre-commit run --all-files`: pre-commit check - runs all validations so commits don't fail.

At this point, we have a pretty workable project stub. There is more that could be added but it is largely project specific.

Commit code.

## Add postgres backend

### Add postgres db with docker support

Add a docker-compose file to start up a postgres container persisting data to a local dir for development use.

See:

* `docker/docker-compose-local.sh`
* `scripts/run-postgres.sh`

Use these commands to:

* Start: `./scripts/run-postgres.sh`
* Stop : `docker-compose -f docker/docker-compose-local.yaml down`

### Setup Django to use postgres

Install Django's postgres support dependency:

```
pip install psycopg2
ᐅ pip freeze
# ...
psycopg2==2.7.5
# ...
```

* Add `psycopg2` to `requirements.txt`
* Add `psycopg2==2.7.5` to `constraints.txt`

In `src/project/settings.py`, replace the `db.sqlite3` DATABASES definition with:

```
URL_WATCHER_DATASTORE_IP = os.getenv('URL_WATCHER_DATASTORE_IP', '127.0.0.1')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dgi',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': URL_WATCHER_DATASTORE_IP,
        'PORT': '5432',
    }
}
```

You can run `./manage.py runserver` to ensure the project comes up cleanly.

Run `./manage.py migrate` to prove connectivity to the database.




