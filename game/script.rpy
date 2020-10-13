# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define e = Character("Eileen")


# El juego comienza aqui.

label start:

    show board

    # Presenta las líneas del diálogo.

    "Mira."
    
    show peon 1:
        function pos1

    "Ahí estás."
    
    show peon 1:
        function pos2
    
    "Ahora te mueves."
    
    "Vamos a testear el script."
    while True:
        $ math_incisos(difficulty("hard"))

    # Finaliza el juego:

    return
