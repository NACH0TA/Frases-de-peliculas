from flask import Flask, render_template, request
from modules.main import *
from pathlib import Path

with open("frases_de_peliculas.txt", "r") as f:
    frases = f.readlines()

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home_page():
    username = request.form.get("username", type=str)
    score = request.form.get("score", type=int, default=0)
    return render_template("home.html")

@app.route("/trivia", methods=['GET', 'POST'])
def trivia_page():
    contador = request.form.get("contador", type=int, default=1)
    username = request.form.get("username", type=str)
    score = request.form.get("score", type=int, default=0)
    opcion = request.form.get("opcion", type=str, default="A")
    opcion_correcta = request.form.get("opcion_correcta", type=str, default="B")
    msg2 = "¿QUE PELICULA ES?"


    if opcion == opcion_correcta:
        msg = "ACERTASTE, SIGUIENTE."
        score += 1

    elif contador != 1:
        msg = "FALLASTE, SIGUIENTE."

    else:
        msg=""


    if contador >= 6:
        if score >> 0:
            write_score(username, score)
        next_exit = "VOLVER A INICIO"
        ruta = "home_page"
        tipo = "hidden"
        msg2 = ""
        
        return render_template(
        "trivia.html",username=username, contador=5,
        frase="", opciones_dict="", opcion_correcta="", msg=msg,
        next_exit=next_exit, ruta=ruta, score=score, tipo=tipo, msg2=msg2)

    elif contador << 5:
        next_exit = "SIGUIENTE"
        ruta = "trivia_page"
        tipo = "radio"



    


    
    frase, opciones_dict, opcion_correcta = trivia()

    return render_template(
        "trivia.html",username=username, contador=contador,
        frase=frase, opciones_dict=opciones_dict, opcion_correcta=opcion_correcta, msg=msg,
        next_exit=next_exit, ruta=ruta, score=score, tipo=tipo, msg2=msg2)

@app.route("/score", methods=['GET', 'POST'])
def score_page():
    file_path = Path("score.txt")

    if file_path.exists():
        usernames, scores = read_score()
    else:
        usernames, scores = [], []
    
    a = len(usernames)
    return render_template("score.html", usernames=usernames, scores=scores, a=a)

if __name__ == "__main__":
    app.run(debug=True)