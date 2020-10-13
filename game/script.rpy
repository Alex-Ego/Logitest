# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define e = Character("Eileen")


# El juego comienza aqui.

label start:

    show tableroplaceholder

    # Presenta las líneas del diálogo.

    "Mira."
    
    show peon:
        function pos1

    "Ahí estás."
    
    show peon:
        linear 0.2 xpos 795 ypos 506 yoffset -60
        linear 0.2 xpos 942 ypos 505 yoffset -60
        linear 0.2 xpos 1107 ypos 393 yoffset -60
        linear 0.2 xpos 1109 ypos 261 yoffset -60
        linear 0.2 xpos 1002 ypos 185 yoffset -60
        linear 0.2 xpos 913 ypos 166 yoffset -60
        linear 0.2 xpos 822 ypos 176 yoffset -60
        linear 0.2 xpos 727 ypos 165 yoffset -60
        linear 0.2 xpos 611 ypos 162 yoffset -60
        linear 0.2 xpos 513 ypos 155 yoffset -60
        linear 0.2 xpos 407 ypos 173 yoffset -60
        linear 0.2 xpos 313 ypos 213 yoffset -60
        linear 0.2 xpos 211 ypos 254 yoffset -60
        linear 0.2 xpos 152 ypos 348 yoffset -60
        linear 0.2 xpos 191 ypos 448 yoffset -60
        linear 0.2 xpos 339 ypos 520 yoffset -60
        linear 0.2 xpos 493 ypos 535 yoffset -60
        linear 0.2 xpos 600 ypos 480
    
    "Ahora te mueves."
    
    show peon:
        function pos1
        
    $ math = int(renpy.input("¿Cuánto es 2 x 4?"))
    
    if math == 8:
        show peon:
            function pos2
        "¡Correcto!"
    else:
        ":)"
    
    "Vamos a testear el script."
    while True:
        $ math_incisos(difficulty("hard"))

    # Finaliza el juego:

    return
