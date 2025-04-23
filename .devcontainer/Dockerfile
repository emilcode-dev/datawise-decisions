FROM python:3.11-slim AS base
LABEL maintainer="emilcode-dev"

# poetry
# https://python-poetry.org/docs/configuration/#using-environment-variables
ENV POETRY_VERSION=2.1.2 \
    POETRY_HOME="/opt/poetry" \
    # do not ask any interactive question
    POETRY_NO_INTERACTION=1

ENV PATH="$POETRY_HOME/bin:$PATH"

# Install system dependencies and Poetry
RUN apt-get update && apt-get install -y --no-install-recommends \
        curl build-essential && \
        rm -rf /var/lib/apt/lists/*

# install poetry - respects $POETRY_VERSION & $POETRY_HOME
RUN curl -sSL https://install.python-poetry.org | python3 -

# -------- Builder stage --------
# FROM base AS builder

# WORKDIR /app
# COPY pyproject.toml poetry.lock LICENSE README.md ./

# # Install only runtime dependencies (without dev dependencies)
# RUN poetry config virtualenvs.create false && \
#         poetry install --only main --no-root

# -------- Development stage --------
FROM base AS development

# Additional dev tooling (e.g. Git, etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
        git && \
        rm -rf /var/lib/apt/lists/*

WORKDIR /app

# COPY pyproject.toml poetry.lock LICENSE README.md ./
# RUN poetry install with dev --no-root

# CMD to launch bash in the dev container
CMD ["bash"]

# -------- Production stage --------
# FROM python:3.12-slim AS production

# # Copy runtime dependencies from builder
# COPY --from=builder /usr/local/lib/python3.12 /usr/local/lib/python3.12
# COPY --from=builder /usr/local/bin /usr/local/bin

# WORKDIR /app

# # Copy application code
# COPY . .

# # Use non-root user for security
# RUN adduser --disabled-password --gecos '' appuser && chown -R appuser /app
# USER appuser

# CMD ["python", "main.py"]
        