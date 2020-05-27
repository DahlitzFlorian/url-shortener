FROM tiangolo/meinheld-gunicorn-flask:python3.7-alpine3.8

ENV POETRY_VERSION=1.0.5

# libressl-dev musl-dev libffi-dev for poetry
RUN apk add --update --no-cache gcc g++ libstdc++ libressl-dev musl-dev libffi-dev && \
    python -m pip install --upgrade pip && \
    python -m pip install "poetry==$POETRY_VERSION"

# Copy only requirements to cache them in docker layer
WORKDIR /app
COPY poetry.lock pyproject.toml /app/

# Project initialization
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-dev

# clean up
RUN apk del \
    gcc \
    g++ && \
    python -m pip uninstall -y poetry

COPY ./app /app
