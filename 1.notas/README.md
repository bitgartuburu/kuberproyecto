# Aplicación de Notas:

En este documento voy a explicar y justificar el proceso de desarrollo de la aplicación de toma de notas

## Primer aproximación 

Para el primer prototipo de esta aplicación, me voy a basar en un par de tutoriales muy clásicos para la creación de listas de tareas y a partir de ahi modificare el esquema.

El esquema tutorizado, parte de la creación de una función principal que imprime las opciones para que el usuario sepa lo que puede hacer. 

```
def menu_tareas():
    print("\n--- Lista de tareas ---")
    print("1. Añadir tarea")
    print("2. Ver tareas")
    print("3. Completar tareas")
    print("4. Borrar tareas")
    print("5. Salir")
```

Esta primera función estará definida en un bucle 'while', que va a mantener nuestro menú mostrandose hasta que el usuario salga de ella a través de la 5 opción. 
Menos a opción de salida, las otras 4 estarán definidas en funciones, y serán llamadas al usuario en un bloque elif.

```
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
```
