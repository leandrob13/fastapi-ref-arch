# Python Reference Architecture 

## Setting up Pipenv:

*Python 3 is required*

The virtual environment is generated with [pipenv](https://pipenv.readthedocs.io/en/latest/).

First install pipenv:

```shell script
pip3 install pipenv
```

In the project's root execute to create the virtual environment with python 3.8:

```shell script
pipenv --python 3.8 
```

For macOS users, python 3.8 is still not supported as the default python formulae. You need to install version 3.8:
```shell script
brew install python@3.8
```

Then you set up the environment as:
```shell script
pipenv  --python /usr/local/opt/python@3.8/bin/python3.8
```

If you already have a requirements.txt file in the root of the project, pipenv will automatically create the Pipfile from it.

Install all the packages specified in the Pipfile:

```shell script
pipenv install --dev
```

When updating dependencies, execute the update command:

```shell script
pipenv update
```

## Executing development tasks

Using the `Invoke` commands, you can control the development tasks. 

Run static type checking with mypy:

```shell script
pipenv run invoke mypy
```

To run the tests with coverage check:

```shell script
pipenv run invoke tests
```

This command will generate the html coverage report and store it htmlcov folder in the project's root directory.

To run `Black` code formatter:

```shell script
pipenv run invoke formatcode
```

To run all the tasks above:

```shell script
pipenv run invoke validate
```

To run the http server:

```shell script
pipenv run invoke run
```

## Packages and tools

- Http Framework: [FastAPI](https://fastapi.tiangolo.com)
- Http Client: [Httpx](https://www.python-httpx.org)
- Http Server: [Hypercorn](https://pgjones.gitlab.io/hypercorn/)
- ORM: [Tortoise](https://tortoise-orm.readthedocs.io/en/latest/index.html)
- Coverage: [Pytest-Cov](https://pytest-cov.readthedocs.io/en/latest)
- Static type check: [MyPy](https://mypy.readthedocs.io/en/stable/)
- Task manager: [Invoke](http://www.pyinvoke.org/index.html) 
