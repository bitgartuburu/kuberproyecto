# 1. Usar la imagen oficial y ligera de Python
FROM python:3.11-slim

# 2. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /home

# 3. Instalar las dependencias de Python directamente (sin pasar por apt)
RUN pip install --no-cache-dir flask requests

# 4. Copiar el código fuente de tu microservicio
COPY notas.py .

# 5. Indicar el comando de ejecución
CMD ["python3", "notas.py"]