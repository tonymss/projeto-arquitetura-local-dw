\# Projeto dbt - Arquitetura Local DW



Este projeto dbt faz parte de uma arquitetura de Data Warehouse desenvolvida em ambiente local utilizando Docker, Apache Airflow e PostgreSQL.



O dbt é responsável pela transformação, organização e validação dos dados dentro do Data Warehouse.



\## Arquitetura



O fluxo de transformação dos dados segue as seguintes camadas:



\*\*PostgreSQL → Bronze → Silver → Gold\*\*



\- \*\*PostgreSQL:\*\* fonte dos dados

\- \*\*Bronze:\*\* preparação inicial dos dados

\- \*\*Silver:\*\* padronização e transformação

\- \*\*Gold:\*\* dados preparados para análise



\## Modelos



\### Bronze



Camada responsável pela preparação inicial dos dados provenientes da origem.



\*\*Modelo:\*\*



`stg\_clientes`



Responsabilidades:



\- Leitura dos dados da tabela de origem

\- Organização dos campos

\- Disponibilização dos dados para as próximas camadas



\### Silver



Camada responsável pela transformação e padronização dos dados.



\*\*Modelo:\*\*



`dim\_clientes`



Transformações realizadas:



\- Remoção de espaços desnecessários

\- Padronização do estado para letras maiúsculas

\- Organização da dimensão de clientes



\### Gold



Camada destinada aos dados preparados para consumo analítico.



\*\*Modelos:\*\*



`clientes\_ativos`



`resumo\_clientes`



O modelo `clientes\_ativos` disponibiliza os clientes atualmente ativos.



O modelo `resumo\_clientes` apresenta um resumo com:



\- Total de clientes

\- Clientes ativos

\- Clientes inativos



\## Qualidade dos dados



O projeto possui testes de qualidade utilizando recursos nativos do dbt.



Testes implementados:



\- `not\_null`

\- `unique`



Os testes verificam principalmente:



\- Campos obrigatórios

\- Unicidade do identificador do cliente

\- Integridade dos dados transformados



\## Execução



Para verificar a configuração do projeto:



```bash

dbt debug

```



Para executar os modelos:



```bash

dbt run

```



Para executar os testes:



```bash

dbt test

```



Para executar modelos e testes em sequência:



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



\## Ambiente



O dbt é executado dentro do ambiente Docker utilizado pelo projeto.



Tecnologias utilizadas:



\- dbt Core

\- PostgreSQL

\- Docker

\- Apache Airflow

