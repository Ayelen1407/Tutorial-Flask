from flask import Flask, url_for, render_template
import sqlite3

app = Flask(__name__)
#------CONEXION A BASE DE DATOS
db=None
def dict_factory(cursor, row):
  """Arma un diccionario con los valores de la fila."""
  fields = [column[0] for column in cursor.description]
  return {key: value for key, value in zip(fields, row)}

def abrirConexion():
    global db
    db = sqlite3.connect("instance/datos.sqlite")
    db.row_factory = dict_factory

def cerrarConexion():
    global db
    if db is not None:
        db.close()
        db = None

@app.route("/test-db")
def testDB():
   abrirConexion()
   cursor = db.cursor()
   cursor.execute("SELECT COUNT(*) AS cant FROM usuarios; ")
   res = cursor.fetchone()
   registros = res["cant"]
   cerrarConexion()
   return f"Hay {registros} registros en la tabla usuarios"

#@app.route("/usuarios/")
#def obterGente():
#    global db
#    conexion = abrirConexion()
#    cursor = conexion.cursor()
#    cursor.execute('SELECT * FROM usuarios')
#    resultado = cursor.fetchall()# fetchall te selecciona todos / fetchone te trae un solo resultado
#    cerrarConexion()
#    fila = [dict(row) for row in resultado]# fila por fila
#    return str(fila)# te lo devuelve en string

#------ EJERCICIO - CREAR RUTAS(3) INSERTAR - BORRAR - MOSTRAR
@app.route("/insertar/<string:usuario>/<string:email>")
def insertar(usuario, email):
    abrirConexion()
    cursor = db.execute("INSERT INTO usuarios(usuario, email) VALUES (?, ?);", (usuario, email))
    db.commit()
    cerrarConexion()
    return "se agregó a ayelen con su email"
    
@app.route("/borrar/<int:id>")
def borrar(id):
    abrirConexion()
    cursor = db.execute("DELETE FROM usuarios WHERE id=?", (id,))
    db.commit()
    cerrarConexion()
    return f"se borro el registro {id}"

@app.route("/mostrar/<int:id>")
def mostrar_nombre_email(id):
    abrirConexion()
    cursor = db.cursor()
    cursor.execute("SELECT usuario, email FROM usuarios WHERE id=?", (id,))
    res = cursor.fetchone()
    cerrarConexion()
    return f"usuario:{res['usuario']} email:{res['email']}"
#------ UNA RUTA USANDO PLANTILLA
@app.route("/mostrar-datos-plantillas/<int:id>")
def datos_plantilla(id):
    abrirConexion()
    cursor = db.cursor()
    cursor.execute("SELECT id, usuario, email, telefono, direccion FROM usuarios WHERE id=?; ", (id,))
    res = cursor.fetchone()
    cerrarConexion()
    usuario = None
    email = None
    telefono= None
    direccion = None
    if res != None:
        usuario=res['usuario']
        email=res['email']
        telefono=res['telefono']
        direccion=res['direccion']
    return render_template("datos.html", id=id, usuario=usuario, email=email, telefono=telefono, direccion=direccion)

    
#------ EJERCICIO EXTRA
@app.route("/insertar/<string:usuario>/<string:email>")
def añadir(usuario, email):
    abrirConexion()
    cursor = db.execute("INSERT INTO usuarios(usuario, email) VALUES (?, ?);", (usuario, email))
    db.commit()
    cerrarConexion()
#------ (falta terminar)

#------ EJERCICIO - Nueva ruta con link 
@app.route("/mostrar-usuarios-plantillas")
def lista_usuarios():
    abrirConexion()
    cursor = db.cursor()
    cursor.execute("SELECT usuario FROM usuarios")
    res = cursor.fetchall()
    cerrarConexion()
    return render_template("lista.html", usuarios = [res])

@app.route("/usuarios")
def usuarios():
     url_mostrar1 = url_for("datos_plantilla", id=1)
     url_mostrar2 = url_for("datos_plantilla", id=2)
     return f"""
    <a href="{url_mostrar1}">andres</a>
    <br>
    <a href="{url_mostrar2}">tomas</a>
    """
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
