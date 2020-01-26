from invoke import task


@task
def publish(ctx):
    """
    Builds wheel and publishes new version to PyPi repo
    """
    _build(ctx)
    # _push(ctx)


def _build(ctx):
    """
    Build package wheel
    """
    ctx.run("rm -rf dist build")
    ctx.run("python3 setup.py sdist bdist_wheel")


def _push(ctx):
    """
    Upload wheel to PyPi repository
    """
    ctx.run("python3 -m twine upload dist/*")
