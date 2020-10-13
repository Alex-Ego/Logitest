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
    
    call c6
    
    "Ahora te mueves."
    
    $ diceRoll()
    
    "Oh mira, un dado"
    
    hide dice
    
    "A ver qué pasa si lo lanzamos otra vez"
    
    $ movement("c1", diceRoll())
    
    "Basado"
    
    #"Wow."
    
    #"Bueno, a ver"
    
    #$ math_incisos("areas")

    # Finaliza el juego:

    return
