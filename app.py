from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def principal():
    url_hola = url_for("consultaxn")
    url_dado = url_for("dado", caras=6)
    url_logo = url_for("static", filename="aquarius.jpg")

    return f"""
    <a href="{url_hola}">Hola</a>
    <br>
    <a href="{url_for("bye")}">Chau</a>
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

#mi ejemplo
@app.route("/consultaxn/<string:nombre>")
def consultaxn(nombre):
    return f"<p>¿Cómo estas {nombre}?</p>"
