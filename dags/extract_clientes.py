from datetime import datetime

import requests
import psycopg2

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator


def extrair_clientes():

    # 1. Busca os dados da API
    response = requests.get(
        "http://projeto_dw_api:8000/clientes",
        timeout=30,
    )

    response.raise_for_status()

    clientes = response.json()

    print(f"Clientes extraídos da API: {len(clientes)}")

    # 2. Conecta no PostgreSQL
    conn = psycopg2.connect(
        host="projeto_dw_postgres",
        port=5432,
        user="dw_user",
        password="dw_password",
        dbname="dw",
    )

    cur = conn.cursor()

    # 3. Overwrite da tabela
    cur.execute("TRUNCATE TABLE origem_clientes")

    # 4. Insere os dados novos
    for cliente in clientes:
        cur.execute(
            """
            INSERT INTO origem_clientes (
                id_cliente,
                nome_cliente,
                cidade,
                estado,
                data_cadastro,
                ativo
            )
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (
                cliente["id_cliente"],
                cliente["nome_cliente"],
                cliente["cidade"],
                cliente["estado"],
                None,
                cliente["ativo"],
            ),
        )

    # 5. Confirma a transação
    conn.commit()

    cur.close()
    conn.close()

    print("Carga de clientes concluída com sucesso!")


with DAG(
    dag_id="clientes_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="0 9 * * *",
    catchup=False,
    tags=["api", "dbt", "dw"],
) as dag:

    extract = PythonOperator(
        task_id="extract_clientes",
        python_callable=extrair_clientes,
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="""
        cd /usr/local/airflow/dbt/projeto_dw &&
        dbt run
        """,
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command="""
        cd /usr/local/airflow/dbt/projeto_dw &&
        dbt test
        """,
    )

    extract >> dbt_run >> dbt_test