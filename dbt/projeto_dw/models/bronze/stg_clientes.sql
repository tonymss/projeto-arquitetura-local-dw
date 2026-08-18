{{ config(materialized='table') }}

SELECT
    id_cliente,
    nome_cliente,
    cidade,
    estado,
    data_cadastro,
    ativo
FROM {{ source('postgres_dw', 'origem_clientes') }}
