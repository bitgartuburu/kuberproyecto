# Aplicación de gestión de notas y lista de tareas
import json
import os

ARCHIVO_TAREAS = "tareas.json"

def cargar_tareas():
    if not os.path.exists(ARCHIVO_TAREAS):
        return []
    try:
        with open(ARCHIVO_TAREAS, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except (json.JSONDecodeError, IOError):
        print("Error al leer archivo JSON. Se iniciará una lista vacía.")
        return []

def guardar_tareas():
    try:
        with open(ARCHIVO_TAREAS, 'w', encoding='utf-8') as archivo:
            json.dump(tareas, archivo, indent=4, ensure_ascii=False)
    except IOError:
        print("Error al guardar las tareas en el disco.")

tareas = cargar_tareas()

def menu_tareas():
    print("\n--- Lista de tareas ---")
    print("1. Añadir tarea")
    print("2. Ver tareas")
    print("3. Completar tareas")
    print("4. Borrar tareas")
    print("5. Salir")

def add_tareas():
    tarea = input("Introduce la tarea: ")
    tareas.append({"tarea":tarea, "done":False})
    guardar_tareas()
    print(f"Tarea '{tarea}' añadida")


def ver_tareas():
    if not tareas:
        print("No hay tareas todavia")
        return
    print("\nTus Tareas")
    for index, tarea in enumerate(tareas, start=1):
        estado = "ok" if tarea["done"] else "not"
        print(f"{index}. {tarea['tarea']} [{estado}]")

def marcar_tareas():
    ver_tareas()
    if not tareas:
        return
    try:
        index = int(input("Introduce el número de tareas que quieres marcar como completa: ")) -1
        if 0 <= index < len(tareas):
            tareas[index]["done"] = True
            guardar_tareas()
            print("Marcada como completada")
        else:
            print("Número no validao")
    except ValueError:
        print("Introduce un número válido por favor.")

def borrar_tareas():
    ver_tareas()
    if not tareas:
        return
    try:
        index = int(input("Introduce el número de tarea que quieres eliminar: ")) -1
        if 0 <= index < len(tareas):
            borrada = tareas.pop(index)
            guardar_tareas()
            print(f"Se ha eliminado la tarea: {borrada['tarea']}")
        else:
            print("Tarea no encontrada")
    except ValueError:
        print("Introduce una tarea válida por favor.")

while True:
    menu_tareas()
    eleccion = input("Elige una opción (1-5): ")

    if eleccion == '1':
        add_tareas()
    elif eleccion == '2':
        ver_tareas()
    elif eleccion == '3':
        marcar_tareas()
    elif eleccion == '4':
        borrar_tareas()
    elif eleccion == '5':
        print("¡Hasta luego!")
        break
    else:
        print("Opción invalida. Prueba otra vez.")
