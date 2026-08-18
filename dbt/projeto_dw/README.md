\# Projeto dbt - Projeto Arquitetura Local DW



Este projeto dbt faz parte da arquitetura de Data Warehouse local desenvolvida com Docker, Apache Airflow e PostgreSQL.



\## Arquitetura



```text

PostgreSQL

&#x20;   ↓

Bronze

&#x20;   ↓

Silver

&#x20;   ↓

Gold

```



\## Camadas



\### Bronze



Responsável pela preparação inicial dos dados provenientes das fontes.



\- `stg\_clientes`



\### Silver



Responsável pela transformação e padronização dos dados.



\- `dim\_clientes`



\### Gold



Camada destinada aos dados prontos para consumo analítico.



\- `clientes\_ativos`

\- `resumo\_clientes`



\## Testes



O projeto possui testes de qualidade utilizando:



\- `not\_null`

\- `unique`



Execução:



```bash

dbt test

```



\## Execução



Para executar os modelos:



```bash

dbt run

```



Para executar os testes:



```bash

dbt test

```



Para executar modelos e testes:



```bash

dbt build

```



\## Estrutura



```text

models/

├── bronze/

│   ├── sources.yml

│   └── stg\_clientes.sql

│

├── silver/

│   ├── dim\_clientes.sql

│   └── schema.yml

│

└── gold/

&#x20;   ├── clientes\_ativos.sql

&#x20;   ├── resumo\_clientes.sql

&#x20;   └── schema.yml

```

