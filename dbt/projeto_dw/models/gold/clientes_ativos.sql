{{ config(materialized='table') }}

SELECT
    id_cliente,
    nome_cliente,
    cidade,
    estado,
    data_cadastro
FROM {{ ref('dim_clientes') }}
WHERE ativo = true
