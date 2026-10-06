#GESTOR DE TAREAS
import json 

def cargar_tareas():
    try:
        with open('tareas.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print('Error: El archivo no se encontro')
        return []
    except json.JSONDecodeError:
        print('Error: El archivo está dañado, empezando con lista vacía')
        return []

def menu():
    while True:
        print("Gestor de tareas")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Completar tarea")
        print("4. Eliminar tareas")
        print("5. Salir")
        opcion = input("Que deseas hacer?:")
        if opcion == '1':
            ver_tareas()
        elif opcion == '2':
            if agregar_tarea():
                guardar_tareas()
        elif opcion == '3':
            if completar_tarea():
                guardar_tareas()
        elif opcion == '4':
            if eliminar_tarea():
                guardar_tareas()
        elif opcion == '5':
            break
        else:
            print('No hay ninguna opcion con ese numero')
            return


def ver_tareas():
    if not tareas:
        print('No hay tareas')
    else:
        for tarea in tareas:
            if tarea['completada']:
                simbolo = ['x']
            else:
                simbolo = ['']
            print(f"{tarea['id_tarea']}. {simbolo} {tarea['titulo']}")

def agregar_tarea():
    titulo = input('Cual es el titulo?: ')
    if not titulo.strip():
        print('Introduce un titulo')
        return
    id_maximo = max([tarea['id_tarea'] for tarea in tareas]) if tareas else 0
    nuevo_id = id_maximo + 1
    
    nueva_tarea = {
        'id_tarea' : nuevo_id,
        'titulo': titulo,
        'completada': False
    }
    tareas.append(nueva_tarea)
    print('tarea Agregada')
    

def completar_tarea():
    try:
        id_tarea = int(input('Que tarea deseas marcar como completada?: '))
        for tarea in tareas:
            if tarea['id_tarea'] == id_tarea:
                tarea['completada'] = True
                print('tarea marcada como completada')
                break
        else:
            print('el id no coincide')
            
    except ValueError:
        print('Error: Ingresaste un valor que no es correcto, ingresa un id/numero valido')
        

def eliminar_tarea():
    try:
        id_tarea = int(input('Que tarea deseas eliminar?: '))
        for tarea in tareas:
            if tarea['id_tarea'] == id_tarea:
                tareas.remove(tarea)
                print('tarea eliminada')
                break
        else:
            print('el id no coincide')
            
    except ValueError:
        print('Error: Ingresaste un valor que no es correcto, ingresa un id/numero valido')
        
        
def guardar_tareas():
    with open('tareas.json', 'w') as file:
        json.dump(tareas, file)
        
tareas = cargar_tareas()
menu()