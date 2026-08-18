{{ config(materialized='table') }}

SELECT
    COUNT(*) AS total_clientes,
    COUNT(*) FILTER (WHERE ativo = true) AS clientes_ativos,
    COUNT(*) FILTER (WHERE ativo = false) AS clientes_inativos
FROM {{ ref('dim_clientes') }}
