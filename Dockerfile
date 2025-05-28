ARG DEBIAN_VERSION=bookworm
ARG UV_VERSION=latest
ARG VARIANT=3.13

FROM ghcr.io/astral-sh/uv:$UV_VERSION AS uv

FROM python:$VARIANT-slim-$DEBIAN_VERSION

WORKDIR /app

COPY --from=uv /uv /uvx /bin/
COPY pyproject.toml uv.lock ./
COPY backend backend
COPY README.md .
COPY LICENSE .

ENV PYTHONDONTWRITEBYTECODE=True
ENV PYTHONUNBUFFERED=True
ENV UV_LINK_MODE=copy

# hadolint ignore=DL3008
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    libgl1 libglib2.0-0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN uv sync --frozen --no-install-project

ENTRYPOINT ["uv", "run", "uvicorn", "backend.__main__:run", "--factory", "--port", "8080", "--host", "0.0.0.0", "--reload"]
