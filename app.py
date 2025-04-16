from flask import Flask, url_for
import sqlite3

app = Flask(__name__)
#------CONEXION A BASE DE DATOS
db=None
def abrirConexion():
    global db
    db = sqlite3.connect("instance/datos.sqlite")
    db.row_factory = sqlite3.Row
    return db

def cerrarConexion():
    global db
    if db is not None:
        db.close()
        db = None

@app.route("/usuarios/")
def obterGente():
    global db
    conexion = abrirConexion()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM usuarios')
    resultado = cursor.fetchall()# fetchall te selecciona todos / fetchone te trae un solo resultado
    cerrarConexion()
    fila = [dict(row) for row in resultado]# fila por fila
    return str(fila)# te lo devuelve en string
#------

@app.route("/")
def principal():
    url_hola = url_for("consultaxn", nombre='Aye')
    url_dado = url_for("dado", caras=6)
    url_logo = url_for("static", filename="aquarius.jpg")

    return f"""
    <a href="{url_hola}">Consulta</a>
    <br>
    <a href="{url_for("respuesta")}">Respuesta</a>
    <br>
    <a href="{url_logo}">Logo</a>
    <br>
    <a href="{url_dado}">Tirar_dado</a>
    """

@app.route("/pregunta")
def pregunta():
    return "<p>¿Cómo estas?</p>"

@app.route("/hola/<string:nombre>")
def saludar_con_nombre(nombre):
    return f"<p>hola {nombre}!</p>"

@app.route("/dado/<int:caras>")
def dado(caras):
    from random import randint
    numero = randint(1,caras)
    return f"<p>dado de {caras} caras, salio {numero}!</p>"

@app.route("/suma/<int:n1>/<int:n2>")
def suma(n1,n2):
    suma = n1 +n2
    return f"<p>{n1} mas {n2} da {suma}</p>"


@app.route("/respuesta")
def respuesta():
    return "<p>Estoy bien</p>"

#------ Mi ejemplo
@app.route("/consultaxn/<string:nombre>")
def consultaxn(nombre):
    return f"<p>¿Cómo estas {nombre}?</p>"
