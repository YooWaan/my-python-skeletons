import nox


@nox.session
def lint(session):
    session.install("pylint", "bandit", "mypy")
    session.run("pylint", "hello")
    session.run("mypy", "hello")
    session.run("bandint", "-r", "hello")
