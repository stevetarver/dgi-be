## Dividend Growth Investment analysis - back-end

## Local dev setup

Install `pyenv`, if not already installed:

```
brew install pyenv
brew install pyenv-virtualenv
```

Create a dedicated virtual-env

```
# Install our base python version - for use with pyenv virtual-envs
pyenv install 3.7.0

# You MUST create the virtual-env specifying the python version to avoid
# 'command not found' errors when running some external tools.
pyenv virtualenv --python=python3.7 3.7.0 dgi-3.7.0
```

Install project dependencies

```
pip install -r requirements-dv.txt
```

Setup pre-commit hooks:

```
pre-commit install
```

Set PyCharm project interpreter:

1. Open PyCharm Preferences -> Project: be -> Project Interpreter
    1. Click the 'Settings' gear icon right of the Project Interpreter
    1. Select 'Existing environment'
    1. Select 'dgi-3.7.0'
    1. OK all dialogs


**NOTE**: See `doc/project-base.md` for PyCharm `pylint` external tool config.

## Common commands

Postgres

```
# Start
./scripts/run-postgres.sh

# Stop
docker-compose -f docker/docker-compose-local.yaml down
```

Run the project

```
./manage.py runserver
```

Run pre-commit checks - to avoid commit failures and periodically check code quality:

```
pre-commit run --all-files
```

Lint a file or directory:

```
pylint file | dir
```
