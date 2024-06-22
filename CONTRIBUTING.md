# Contributing to fs.sharepointfs

This project depends on the following utilities for development:

- The python versions are managed by [pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#automatic-installer).
- The environment isolation and package build/publish use [poetry](https://python-poetry.org/).
- The formatter is [black](https://black.readthedocs.io/en/stable/).
- The linter is [ruff](https://docs.astral.sh/ruff/).
- The testing tool is [tox](https://tox.wiki/en/latest/user_guide.html).
- [pre-commit](https://pre-commit.com/) forces some work done before commit.

## Development Environment Setup

### pyenv

Multiple python versions (3.8 ~ 3.11) will be tested. We need to install and enable those python versions by pyenv.

```bash
curl https://pyenv.run | bash

pyenv install python3.8
pyenv install python3.9
pyenv install python3.10
pyenv install python3.11

# Clone the code
git clone git@github.com:foreverfaint/fs-sharepointfs.git

cd fs-sharepointfs
# We must enable all the testing target versions in the working folder, then `tox` will automatically discover the python executables for virtual environment setup.
pyenv local python3.8 python3.9 python3.10 python3.11

# The default python is the first python version passed to `pyenv local` command.
# You can verify it by running
$ python --version
python 3.8.*
```

### poetry

```bash
curl -sSL https://install.python-poetry.org | python -

# 1. create a new virtual environment defined by pyproject.toml
# 2. install all the dependences
# 3. use editable installation to install the root package fs.sharepointfs
poetry install -vvv

# You should see the python executable from a new isolated path.
which python
```

### ruff

`ruff` is configured via the file `pyproject.ini`. We prefer `ruff` to `flake8` because of `pyproject.ini` support.

```bash
poetry add -G dev ruff

ruff check
```

### black

`black` is configured via the file `pyproject.toml`.

```bash
black
```

### tox

`tox` is configured via the file `tox.ini`.

### pre-commit

`pre-commit` will enforce to run `ruff` and `black` before committing. It is configured by `.pre-commit-config.yaml`.

```bash
# Every time you clone a project using pre-commit running pre-commit install should always be the first thing you do.
pre-commit install

# Run against all the files explicitly
pre-commit run --all-files
```
