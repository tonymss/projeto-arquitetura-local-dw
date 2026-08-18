# Projeto Arquitetura Local DW

Projeto de Engenharia de Dados desenvolvido para estudar e aplicar uma arquitetura de Data Warehouse local utilizando Docker, Apache Airflow, PostgreSQL, dbt e uma API REST.

## Arquitetura

```text
API REST
   ↓
Apache Airflow
   ↓
PostgreSQL
   ↓
dbt
   ↓
Bronze → Silver → Gold
```

## Tecnologias

- Python
- FastAPI
- Apache Airflow
- PostgreSQL
- dbt
- Docker
- Git / GitHub

## Pipeline

### 1. Extração

A DAG `clientes_pipeline` é responsável por:

- Consumir dados da API REST
- Validar a resposta
- Conectar ao PostgreSQL
- Carregar os dados na tabela de origem
- Utilizar overwrite para a carga de clientes

### 2. Transformação

O dbt organiza as transformações em três camadas:

**Bronze**
- `stg_clientes`

**Silver**
- `dim_clientes`

**Gold**
- `clientes_ativos`
- `resumo_clientes`

### 3. Qualidade

O dbt executa testes de qualidade dos dados, incluindo:

- `not_null`
- `unique`

## Estrutura do projeto

```text
projeto_arquitetura_dw/
│
├── api/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── dags/
│   ├── clientes_pipeline.py
│   └── .airflowignore
│
├── dbt/
│   └── projeto_dw/
│       ├── models/
│       │   ├── bronze/
│       │   ├── silver/
│       │   └── gold/
│       ├── dbt_project.yml
│       └── profiles.yml
│
├── docker-compose.dw.yml
├── docker-compose.override.yml
├── Dockerfile
└── requirements.txt
```

## Objetivo

O objetivo deste projeto é construir uma arquitetura de dados completa em ambiente local, aplicando conceitos de:

- ingestão de dados
- orquestração
- Data Warehouse
- transformação com dbt
- modelagem dimensional
- testes de qualidade
- containerização
- versionamento com Git

## Próximas etapas

- [ ] Pipeline incremental de vendas
- [ ] Modelagem de fatos e dimensões
- [ ] Modelos incrementais com dbt
- [ ] Mais testes de qualidade
- [ ] CI/CD
- [ ] Migração da arquitetura para cloud
- [ ] Implementação na GCP