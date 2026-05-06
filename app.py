from flask import Flask, render_template, request, abort, redirect
from funciones import *

app = Flask(__name__)

datos=cargarDatos('toyota-modificado.json')

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/items')
def items():
    busqueda = request.args.get('busqueda', '')
    modelo_sel = request.args.get('modelo', '')
    orden = request.args.get('orden', 'asc')
    modelos_disp = obtenerModelos(datos)
    
    
    print(busqueda, modelo_sel, orden)
    
    
    return render_template('items.html',
                           modelos = modelos_disp,
                           busqueda = busqueda,
                           modelo_sel = modelo_sel,
                           modelos_disp = modelos_disp,
                           orden = orden)

app.run('0.0.0.0', 5000, debug=True)
