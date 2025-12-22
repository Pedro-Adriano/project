FROM python:3.11-slim AS development

WORKDIR /backend

# Dependências do sistema (mínimo)
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Poetry
RUN pip install poetry

# Copia apenas os arquivos de dependência (cache)
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root

# Copia o código
COPY . .

CMD ["poetry", "run", "uvicorn", "app.main:application", "--host", "0.0.0.0", "--port", "8899", "--reload"]
