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
    resultados = []
    
    for c in datos:
        nombre = c['name']
        ciudad = c['city']
        estado = c['state']
        inventario = c['inventario']
        
        if busqueda.lower() not in nombre.lower() and busqueda.lower() not in ciudad.lower():
            continue
        
        if modelo_sel and (modelo_sel not in inventario):
            continue
        
        stock_total = calcularStockTotal(inventario)
        
        num_modelos = len(inventario)
        
        resultados.append({
            'code': c['code'],
            'name': nombre,
            'city': ciudad,
            'stock_total': stock_total,
            'num_modelos': num_modelos,
        })
        
    resultados.sort(key=lambda x: x['name'], reverse=(orden == 'desc'))
    
    return render_template('items.html',
                           modelos = modelos_disp,
                           busqueda = busqueda,
                           modelo_sel = modelo_sel,
                           orden = orden,
                           resultados = resultados
                           )

@app.route('/item/<code>')
def detalle(code):
    concesionario = buscarConcesionario(datos, code)
    
    if concesionario is None:
        abort(404)

    return render_template('concesionarios.html', c=concesionario)

app.run('0.0.0.0', 5000, debug=True)
