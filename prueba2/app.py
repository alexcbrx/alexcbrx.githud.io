from flask import Flask, render_template, request, redirect, url_for, send_file
import os
import mysql.connector
import pdfkit
from PIL import Image
from flask import make_response
import base64
from flask import send_file

app = Flask(__name__, template_folder='templates')

# Configuración de la conexión a la base de datos
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'XcuberoX',
    'database': 'integradora',
}


# Función para conectar a la base de datos
def conectar():
    try:
        conexion = mysql.connector.connect(**db_config)
        if conexion.is_connected():
            return conexion
    except mysql.connector.Error as e:
        print(f'Error de conexión: {e}')
        return None

# Rutas de la aplicación

app = Flask(__name__, static_folder='templates', static_url_path='/templates')

@app.route('/')
def animado():
    return render_template('animado.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/rectoria')
def rectoria():
    return render_template('rectoria.html')


@app.route('/psicologia')
def psicologia():
    return render_template('psicologia.html')


@app.route('/libreria')
def libreria():
    return render_template('libreria.html')    

@app.route('/finanzas')
def finanzas():
    return render_template('finanzas.html')

@app.route('/reglamento')
def reglamento():
    return render_template('reglamento.html')  

@app.route('/vinculacion')
def vinculacion():
    return render_template('vinculacion.html')  

@app.route('/prensa')
def prensa():
    return render_template('prensa.html')            

if __name__ == '__main__':
    app.run(debug=True)
