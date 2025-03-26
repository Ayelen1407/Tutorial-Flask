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

@app.route("/respuesta")
def respuesta():
    return "<p>Estoy bien</p>"