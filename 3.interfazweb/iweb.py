# Interfaz web que aglutina la aplicación de notas y el calendario
from flask import Flask, render_template_string
import requests

app = Flask(__name__)

# URLs de comunicación con los otros microservicios
# (En entorno local usarán localhost y sus respectivos puertos; en Kubernetes usarán los nombres de servicio)
NOTAS_URL = "http://notas-service:5000/notas"
CALENDARIO_URL = "http://calendario-service:5001/eventos"


@app.route("/")
def index():
  # 1. Obtenemos las notas del microservicio 1
  try:
    res_notas = requests.get(NOTAS_URL, timeout=2)
    notas = res_notas.json() if res_notas.status_code == 200 else []
  except requests.exceptions.RequestException:
    notas = []

  # 2. Obtenemos los eventos del microservicio 2
  try:
    res_eventos = requests.get(CALENDARIO_URL, timeout=2)
    eventos = res_eventos.json() if res_eventos.status_code == 200 else []
  except requests.exceptions.RequestException:
    eventos = []

  # 3. HTML incrustado con diseño limpio y Bootstrap
  html_template = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Panel Central - Microservicios</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="bg-light">
        <div class="container py-5">
            <h1 class="mb-4 text-center text-primary">Panel de Control de Microservicios</h1>
            
            <div class="row">
                <!-- Sección de Notas -->
                <div class="col-md-6">
                    <div class="card shadow-sm mb-4">
                        <div class="card-header bg-dark text-white">Notas y Tareas</div>
                        <div class="card-body">
                            <ul class="list-group">
                                {% for nota in notas %}
                                    <li class="list-group-item d-flex justify-content-between align-items-center">
                                        {{ nota.tarea }}
                                        <span class="badge bg-{{ 'success' if nota.done else 'warning' }}">
                                            {{ 'Completada' if nota.done else 'Pendiente' }}
                                        </span>
                                    </li>
                                {% else %}
                                    <li class="list-group-item text-muted">No hay notas o el servicio no responde.</li>
                                {% endfor %}
                            </ul>
                        </div>
                    </div>
                </div>

                <!-- Sección de Calendario -->
                <div class="col-md-6">
                    <div class="card shadow-sm mb-4">
                        <div class="card-header bg-dark text-white">Calendario y Eventos</div>
                        <div class="card-body">
                            <ul class="list-group">
                                {% for evento in eventos %}
                                    <li class="list-group-item">
                                        <div class="d-flex w-100 justify-content-between">
                                            <h5 class="mb-1">{{ evento.titulo }}</h5>
                                            <small class="text-muted">{{ evento.fecha }}</small>
                                        </div>
                                        <p class="mb-1 text-secondary">{{ evento.descripcion }}</p>
                                        {% if evento.tarea_asociada %}
                                            <small class="text-primary">🔗 Tarea vinculada: {{ evento.tarea_asociada }}</small>
                                        {% endif %}
                                    </li>
                                {% else %}
                                    <li class="list-group-item text-muted">No hay eventos o el servicio no responde.</li>
                                {% endfor %}
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
  return render_template_string(html_template, notas=notas, eventos=eventos)


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000)