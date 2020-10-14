
# El juego comienza aqui.

label start:

    show sea:
        zoom 3.0
        ease 20.0 xpan 500 ypan 400
        ease 20.0 xpan -500 ypan -400
        ease 20.0 xpan 250
        ypan 250
        ease 20.0 xpan -250 ypan -250
        repeat

    show board
    
    show screen score_count(score)
    
    "¡Bienvenido a Logitest!"
    
    "¡Llega a 15 puntos para ganar!"
    
    jump inicio

label win:
    return