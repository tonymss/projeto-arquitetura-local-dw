from fastapi import FastAPI

app = FastAPI(title="API de Clientes")


@app.get("/clientes")
def listar_clientes():
    return [
        {
            "id_cliente": 1,
            "nome_cliente": "Joao Silva",
            "cidade": "Novo Hamburgo",
            "estado": "RS",
            "ativo": True
        },
        {
            "id_cliente": 2,
            "nome_cliente": "Maria Souza",
            "cidade": "Porto Alegre",
            "estado": "RS",
            "ativo": True
        },
        {
            "id_cliente": 3,
            "nome_cliente": "Carlos Oliveira",
            "cidade": "Sao Leopoldo",
            "estado": "RS",
            "ativo": False
        },
        {
            "id_cliente": 4,
            "nome_cliente": "Ana Santos",
            "cidade": "Canoas",
            "estado": "RS",
            "ativo": True
        },
        {
            "id_cliente": 5,
            "nome_cliente": "Pedro Costa",
            "cidade": "Gravatai",
            "estado": "RS",
            "ativo": True
        }
    ]