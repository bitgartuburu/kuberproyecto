from flask import Flask, jsonify, request
import json
import os

# Inicializamos la aplicación Flask
app = Flask(__name__)

ARCHIVO_TAREAS = "tareas.json"


def cargar_tareas():
  if not os.path.exists(ARCHIVO_TAREAS):
    return []
  try:
    with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as archivo:
      return json.load(archivo)
  except (json.JSONDecodeError, IOError):
    print("Error al leer archivo JSON. Se iniciará una lista vacía.")
    return []


def guardar_tareas(tareas):
  try:
    with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as archivo:
      json.dump(tareas, archivo, indent=4, ensure_ascii=False)
  except IOError:
    print("Error al guardar las tareas en el disco.")


# 1. GET: Consultar todas las tareas (Sustituye al menú opción 2)
@app.route("/notas", methods=["GET"])
def ver_notas():
  tareas = cargar_tareas()
  return jsonify(tareas), 200


# 2. POST: Añadir una nueva tarea (Sustituye al menú opción 1)
@app.route("/notas", methods=["POST"])
def añadir_nota():
  tareas = cargar_tareas()
  datos = request.get_json()

  if not datos or "tarea" not in datos:
    return jsonify({"error": "Falta el contenido de la tarea"}), 400

  nueva_tarea = {"tarea": datos["tarea"], "done": False}
  tareas.append(nueva_tarea)
  guardar_tareas(tareas)

  return (
      jsonify(
          {"mensaje": f"Tarea '{nueva_tarea['tarea']}' añadida", "nota": nueva_tarea}
      ),
      201,
  )


# 3. PUT: Marcar tarea como completada (Sustituye al menú opción 3)
@app.route("/notas/<int:index>/completar", methods=["PUT"])
def marcar_nota(index):
  tareas = cargar_tareas()
  if 0 <= index < len(tareas):
    tareas[index]["done"] = True
    guardar_tareas(tareas)
    return (
        jsonify({"mensaje": "Marcada como completada", "nota": tareas[index]}),
        200,
    )
  return jsonify({"error": "Número de tarea no válido"}), 404


# 4. DELETE: Borrar una tarea (Sustituye al menú opción 4)
@app.route("/notas/<int:index>", methods=["DELETE"])
def borrar_nota(index):
  tareas = cargar_tareas()
  if 0 <= index < len(tareas):
    borrada = tareas.pop(index)
    guardar_tareas(tareas)
    return (
        jsonify({"mensaje": f"Se ha eliminado la tarea: {borrada['tarea']}"}),
        200,
    )
  return jsonify({"error": "Tarea no encontrada"}), 404


# Arranque del servidor web en el contenedor
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)