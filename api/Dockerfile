FROM python:3.12-slim

WORKDIR /app

COPY api/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY api ./api

CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]
