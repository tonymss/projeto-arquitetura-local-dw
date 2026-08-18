{{ config(materialized='table') }}

SELECT
    id_cliente,
    TRIM(nome_cliente) AS nome_cliente,
    TRIM(cidade) AS cidade,
    UPPER(estado) AS estado,
    data_cadastro,
    ativo
FROM {{ ref('stg_clientes') }}
