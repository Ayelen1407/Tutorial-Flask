from flask import Flask

app = Flask(__name__)

@app.route("/")
def principal():
    return """
        <a href='/pregunta'>pregunta</a>
        <a href='/respuesta'>respuesta</a>
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

#mi ejemplo
@app.route("/consulta/<string:nombre>")
def pregunta_con_nombre(nombre):
    return f"<p>¿Cómo estas {nombre}?!</p>"