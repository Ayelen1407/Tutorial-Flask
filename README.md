# Tutorial-Flask
1- python -m venv .venv <!--para crear el entorno virtual>
2- source .venv/bin/activate <!--para activar el entorno virtual>
3- pip install flask <!--para instalar el flask>
4- flask --version <!--para ver la version de flask>
flask run
flask run --debug <!-- te detecta los cambios y los errores>

cursor.execute() <!--dentro del parentesis se pone la consulta que queres hacer>
cursor.fetchone() <!--devuelve el diguiente registro en la lista>
cursor.fetchall() <!--devuelve los registros que quedan en una lista>
db.commit() <!--para confirmar los cambios>
db.cursor() <!--para pedir un cursor nuevo>
db.execute() <!--crea un cursor nuevo y se crea/hace la consulta(se guarda dentro de una variable)>
db.close() <!--cierra ¿?>
template <!--plantilla - la informacion se puede modificar (tiene huecos donde se puede rellenar, tiene un proceso de envio)>
archivo static <!--la informacion se mantiene, ej:css(es siempre igual) tiene una sola ruta y pagina>