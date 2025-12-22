# 🎬 Movielist API

Este projeto implementa uma API RESTful para processamento e consulta de dados de filmes vencedores do prêmio Golden Raspberry Awards.

A aplicação permite:
- Importar um arquivo CSV com filmes e produtores
- Calcular o menor e o maior intervalo entre prêmios consecutivos
- Retornar os dados estruturados em um dicionário contendo os produtores com menor e maior intervalo entre prêmios.

---

## 🧱 Arquitetura

O projeto segue uma separação clara de responsabilidades:

- API (Routers)
- Services (regras de negócio)
- Repositories (persistência)
- Entities (SQLAlchemy)
- Schemas (Pydantic)

---

## 🐳 Pré-requisitos

Antes de executar o projeto, é necessário instalar:

Docker  
https://docs.docker.com/get-docker/

Docker Compose  
https://docs.docker.com/compose/install/

⚠️ Não é necessário instalar Python ou banco de dados localmente.

---

## ▶️ Como Executar o Projeto

Clone o repositório:

git clone <url-do-repositorio>  
cd project-root  

Suba a aplicação:

docker compose build && docker compose up

Ao subir a aplicação:
- O banco de dados em memória é criado
- O arquivo CSV é importado automaticamente
- A API fica pronta para uso

---

## 📥 Importação do CSV

### Importação automática
O arquivo data/movielist.csv é importado automaticamente no startup da aplicação.

### Importação manual (opcional)

POST /api/import

Este endpoint existe apenas como apoio e não é obrigatório.

---

## 🔍 Consulta de Intervalos

Endpoint principal:

GET /api/intervals

Exemplo de resposta:

{
  "min": [
    {
      "producer": "Producer Name",
      "interval": 1,
      "previousWin": 1990,
      "followingWin": 1991
    }
  ],
  "max": [
    {
      "producer": "Another Producer",
      "interval": 10,
      "previousWin": 2000,
      "followingWin": 2010
    }
  ]
}

---

## 📑 Documentação da API

Swagger UI  
http://localhost:8900/movielist/v1/docs

OpenAPI JSON  
http://localhost:8900/movielist/v1/openapi.json

---

## 🗄️ Modelo de Dados

O banco de dados utiliza um modelo relacional simples, focado em normalização e clareza.

### 🎬 Movies
Armazena os filmes importados do arquivo CSV.

Campos principais:
- `id`: Identificador do filme
- `year`: Ano de lançamento
- `title`: Título do filme
- `studios`: Estúdios responsáveis
- `winner`: Indica se o filme foi vencedor

### 🎥 Producers
Armazena os produtores de filmes.

Campos principais:
- `id`: Identificador do produtor
- `name`: Nome do produtor (único)

### 🔗 Movie_Producers
Tabela associativa responsável pelo relacionamento muitos-para-muitos entre filmes e produtores.

Campos:
- `movie_id`: Referência ao filme
- `producer_id`: Referência ao produtor

📌 Um filme pode possuir múltiplos produtores, e um produtor pode estar associado a múltiplos filmes.

---

## 📦 Gerenciamento de Dependências

O projeto utiliza Poetry:

- pyproject.toml
- poetry.lock

⚠️ Não é necessário executar o Poetry localmente, pois o Docker gerencia o ambiente.

---

## Testes

Para rodar os testes do projeto, utilize o seguinte comando dentro do container:

```bash
docker compose exec project_backend poetry run env PYTHONPATH=/backend pytest

---

## 🏁 Conclusão

Projeto desenvolvido com foco em:
- Boas práticas REST
- Clareza arquitetural
- Facilidade de execução e avaliação