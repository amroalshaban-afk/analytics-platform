# Stage 1: Build Dependencies
FROM python:3.12-slim AS builder

ENV PYTHONUNBUFFERED = 1 \
    PYTHONDONTWRITETOBYTECODE = 1 \
    UV_COMPILE_BYTECODE = 1 \
    VIRTUAL_ENV = /opt/venv \
    PATH = "/opt/venv/bin:$PATH"


RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir uv

WORKDIR /app
COPY . .

RUN python -m venv "$VIRTUAL_ENV" && \
    pip install --no-cache-dir -e ".[dev]"


# Stage 2: Run Tests
FROM builder AS tester
COPY . .
RUN uv sync --extra dev
RUN pytest -q

# Stage 3: Runtime
FROM builder AS runtime

ENV PYTHONUNBUFFERED = 1 \
    PYTHONDONTWRITETOBYTECODE = 1 \
    UV_COMPILE_BYTECODE = 1 \
    VIRTUAL_ENV = /opt/venv \
    PATH = "/opt/venv/bin:$PATH"

WORKDIR /app
COPY --from=builder /opt/venv /opt/venv
COPY . .

EXPOSE 8000
CMD ["python", "main.py"]