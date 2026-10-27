FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Gunicorn levanta la app de Flask en el puerto 8000 con 4 workers concurrentes
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]