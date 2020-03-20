from invoke import task

@task
def format_code(c):
    print("Running black formatter")
    c.run("pipenv run black src")


@task
def mypy(c):
    print("Running mypy")
    c.run("pipenv run mypy src")

@task
def tests(c):
    print("Running pytest")
    c.run("pipenv run pytest --cov=src")
    c.run("pipenv run coverage html -i")


@task(mypy, format_code, tests)
def validate(c):
    print("DONE")

@task
def run(c):
    c.run("pipenv run python -m src.http.main")
