from modules.main import *

inicio = """
#######################################
#  Películas: Preguntas y respuestas  #
#######################################

Elige una opción:

1 - Mostrar lista de películas.
2 - ¡Trivia de película!
3 - Mostrar secuencia de opciones seleccionadas previamente.
4 - Borrar historial de opciones.
5 - Salir"""

print(inicio)
op=input()

if op == 1:
    list_films()
if op == 2:
    frase, diccionario, opcion_correcta =trivia()
    titulo = f"""
     1- {diccionario[1]}
     2- {diccionario[2]}
     3- {diccionario[3]}"""
    
    print("¿De que pelicula es la siguiente frase?")
    print(frase)
    print(titulo)

    op = input()

    if op == 1:
        if diccionario[1] == opcion_correcta:
            print("ACERTASTE")
        else:
            print("FALLASTE")

    if op == 2:
        if diccionario[2] == opcion_correcta:
            print("ACERTASTE")
        else:
            print("FALLASTE")
    
    if op == 3:
        if diccionario[3] == opcion_correcta:
            print("ACERTASTE")
        else:
            print("FALLASTE")

if op == 3:
    show_history()

if op == 4:
    clean_history()

if op == 5:
    pass