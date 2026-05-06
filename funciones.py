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


def calcularStockTotal(inventario):
    stock_total = 0
    for modelo in inventario.values():
        stock_total = stock_total + modelo['stock']
    return stock_total

def buscarConcesionario(datos, code):
    for c in datos:
        if c.get('code') == code:
            return c
    return None

