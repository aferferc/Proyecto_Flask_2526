import json
import sys


def cargarDatos(ruta):
    try:
        with open(ruta, encoding='utf-8') as fichero:
            datos = json.load(fichero)
        return datos
    except FileNotFoundError:
        print('Error al cargar datos: no se encontró el fichero', ruta)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print('Error al leer el JSON:', e)
        sys.exit(1)


def obtenerModelos(datos):
    modelos = []
    for c in datos:
        for modelo in c['inventario']:
            if modelo not in modelos:
                modelos.append(modelo)
    sorted(modelos)
    return modelos




