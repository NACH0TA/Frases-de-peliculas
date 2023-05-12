import random
import datetime
frases, peliculas = [], []
with open("frases_de_peliculas.txt") as file:
    for line in file:
        frase, pelicula = line.split(";")
        frases.append(frase)
        peliculas.append(pelicula.rstrip("\n"))


inicio = """
#######################################
#  Películas: Preguntas y respuestas  #
#######################################
Elige una opción
1 - Mostrar lista de películas.
2 - ¡Trivia de película!
3 - Mostrar secuencia de opciones seleccionadas previamente.
4 - Borrar historial de opciones.
5 - Salir"""

#print(inicio)

#opcion = int(input())

def list_films():
    frases, peliculas = [], []
    with open("frases_de_peliculas.txt") as file:
        for line in file:
            frase, pelicula = line.split(";")
            frases.append(frase)
            peliculas.append(pelicula.rstrip("\n"))
    film_list = []
    i = 0
    for pelicula in sorted(peliculas):
        i = i + 1
        film_list.append(f"{i}- {pelicula}")
    with open("historial.txt", "a") as h:
        h.write(str(datetime.datetime.now()))
        h.write(" Se eligió la opcion 1\n")
    
    return film_list

def trivia():
    valor = random.randint(0, len(frases) - 1)

    frase = frases.pop(valor)
    opcion_correcta = peliculas.pop(valor)
    #print(opcion_correcta)

    valor = random.randint(0, len(peliculas)- 1)
    opcion_incorrecta1 = peliculas[valor]
    while opcion_incorrecta1 == opcion_correcta:
        valor = random.randint(0, len(peliculas)- 1)
        opcion_incorrecta1 = peliculas[valor]

    valor = random.randint(0, len(peliculas)- 1)
    opcion_incorrecta2 = peliculas[valor]
    while opcion_incorrecta2 == opcion_correcta or opcion_incorrecta2 == opcion_incorrecta1:
        valor = random.randint(0, len(peliculas)- 1)
        opcion_incorrecta2 = peliculas[valor]
    
    opciones = [opcion_incorrecta1, opcion_incorrecta2, opcion_correcta]

    diccionario = {1: opciones.pop(random.randint(0,2)), 2: opciones.pop(random.randint(0,1)), 3: opciones.pop()}
    titulo = f"""
    1- {diccionario[1]}
    2- {diccionario[2]}
    3- {diccionario[3]}"""

    #print(titulo)

    #opcion = diccionario[int(input())]
    #if opcion == opcion_correcta:
     #   print("Acertaste!! Felicitaciones te ganaste un 0km!!")
    #else:
     #   print("burro")
    with open("historial.txt", "a") as h:
        h.write(str(datetime.datetime.now()))
        h.write(" Se eligió la opcion 2\n")
    
    return frase , diccionario, opcion_correcta


def history():
    with open("historial.txt", "a") as h:
        h.write(str(datetime.datetime.now()))
        h.write(" Se eligió la opcion 3\n")
    with open("historial.txt", "r") as h:
        for line in h:
            print(line)

def clean_history():
    with open("historial.txt", "w"):
        pass

#if opcion == 5:
    #with open("historial.txt", "a") as h:
        #h.write(str(datetime.datetime.now()))
        #h.write(" Se eligió la opcion 5\n")
    #print("Saludos!")

def write_score(username:str, new_score):
    scores_usernames = []
    with open("score.txt", "a") as s:
        s.write(username +" ")
        s.write(str(new_score))
    with open("score.txt", "r") as s:
        for line in s:
            username, score = line.split(" ")
            scores_usernames.append([int(score.rstrip("\n")), username])
            scores_usernames.sort(reverse=True)
    with open("score.txt", "w") as s:
        for score_username in scores_usernames:
            s.write(score_username[1])
            s.write(" ")
            s.write(str(score_username[0]))
            s.write("\n")

def read_score():
    usernames = []
    scores = []
    with open("score.txt", "r") as s:
        for line in s:
            username, score = line.split(" ")
            scores.append(score.rstrip("\n"))
            usernames.append(username)
        return usernames, scores