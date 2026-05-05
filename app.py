from flask import Flask, render_template, request, abort, redirect

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/items')
def items():
    return render_template('items.html')

app.run('0.0.0.0', 5000, debug=True)
