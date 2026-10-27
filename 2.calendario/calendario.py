# Aplicacion de calendario
from flask import Flask, jsonify, request
import json
import os

# Inicializamos la aplicación Flask para el calendario
app = Flask(__name__)

ARCHIVO_CALENDARIO = "calendario.json"


def cargar_eventos():
  if not os.path.exists(ARCHIVO_CALENDARIO):
    return []
  try:
    with open(ARCHIVO_CALENDARIO, "r", encoding="utf-8") as archivo:
      return json.load(archivo)
  except (json.JSONDecodeError, IOError):
    return []


def guardar_eventos(eventos):
  try:
    with open(ARCHIVO_CALENDARIO, "w", encoding="utf-8") as archivo:
      json.dump(eventos, archivo, indent=4, ensure_ascii=False)
  except IOError:
    print("Error al guardar los eventos en el disco.")


# 1. GET: Consultar todos los eventos del calendario
@app.route("/eventos", methods=["GET"])
def ver_eventos():
  eventos = cargar_eventos()
  return jsonify(eventos), 200


# 2. POST: Crear un nuevo evento (permitiendo asociarlo a una tarea)
@app.route("/eventos", methods=["POST"])
def añadir_evento():
  eventos = cargar_eventos()
  datos = request.get_json()

  if not datos or "titulo" not in datos or "fecha" not in datos:
    return jsonify({"error": "Faltan datos obligatorios (titulo y fecha)"}), 400

  nuevo_evento = {
      "titulo": datos["titulo"],
      "fecha": datos["fecha"],
      "descripcion": datos.get("descripcion", ""),
      "tarea_asociada": datos.get(
          "tarea_asociada", None
      ),  # Permite vincularlo con notas/tareas
  }

  eventos.append(nuevo_evento)
  guardar_eventos(eventos)

  return (
      jsonify({"mensaje": "Evento creado correctamente", "evento": nuevo_evento}),
      201,
  )


# 3. DELETE: Borrar un evento por su índice
@app.route("/eventos/<int:index>", methods=["DELETE"])
def borrar_evento(index):
  eventos = cargar_eventos()
  if 0 <= index < len(eventos):
    borrado = eventos.pop(index)
    guardar_eventos(eventos)
    return (
        jsonify(
            {"mensaje": f"Se ha eliminado el evento: {borrado['titulo']}"}
        ),
        200,
    )
  return jsonify({"error": "Evento no encontrado"}), 404


# Arranque del servidor web en el puerto 5001 (distinto al de notas para evitar conflictos)
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5001)