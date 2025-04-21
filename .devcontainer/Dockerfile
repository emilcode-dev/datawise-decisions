# Use Ubuntu 24.04 LTS as the base image
FROM python:3.11 as base
LABEL maintainer="emilcode-dev"

    # python
    ENV PYTHONUNBUFFERED=1 \
    # prevents python creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    \
    # poetry
    # https://python-poetry.org/docs/configuration/#using-environment-variables
    POETRY_VERSION=1.8.2 \
    # make poetry install to this location
    POETRY_HOME="/opt/poetry" \
    # make poetry create the virtual environment in the project's root
    # it gets named `.venv`
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    # do not ask any interactive question
    POETRY_NO_INTERACTION=1 \
    \
    # paths
    # this is where our requirements + virtual environment will live
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"


# prepend poetry and venv to path
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"




# `builder-base` stage is used to build deps + create our virtual environment
FROM base as builder
RUN apt-get update && apt-get install -y --no-install-recommends\
        # deps for installing poetry
        curl \
        # deps for building python deps
        build-essential \
        && rm -rf /var/lib/apt/lists/*

# install poetry - respects $POETRY_VERSION & $POETRY_HOME
curl -sSL https://install.python-poetry.org | python3 -

# copy project requirement files here to ensure they will be cached.
WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./

# install runtime deps - uses $POETRY_VIRTUALENVS_IN_PROJECT internally
RUN poetry install --only main


# `development` image is used during development / testing
FROM base as development

RUN apt-get update && apt-get install -y --no-install-recommends\
        git \
        && rm -rf /var/lib/apt/lists/*  

WORKDIR $PYSETUP_PATH

# copy in our built poetry + venv
COPY --from=builder $POETRY_HOME $POETRY_HOME
COPY --from=builder $PYSETUP_PATH $PYSETUP_PATH

# quicker install as runtime deps are already installed
RUN poetry install --with dev

# will become mountpoint of our code
WORKDIR /app


# # `production` image used for runtime
# FROM base as production

# COPY --from=builder $PYSETUP_PATH $PYSETUP_PATH
# COPY ./app /app/
# WORKDIR /app