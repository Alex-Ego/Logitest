################################################################################
## Funciones
################################################################################

image dice roll:
        parallel:
            "dice 1"
            linear 0.1
            "dice 2"
            linear 0.1
            "dice 3"
            linear 0.1
            "dice 4"
            linear 0.1
            "dice 5"
            linear 0.1
            "dice 6"
            linear 0.1
            repeat
        parallel:
            center zoom 0.25
            linear 2.0 truecenter zoom 1
        parallel:
            rotate 0
            linear 0.5 rotate 360
            repeat

label show_tickets:
    $ tickets = True
    show screen tickets
    "¡Obtuviste un ticket de pase!"

init -5 python:
    import random
    
    def diceRoll():
        renpy.play("audio/diceshake.mp3")
        renpy.show("dice roll")
        renpy.say(None, "Tirando el dado...")
        random.seed()
        dice_num = random.randint(1, 6)
        if dice_num == 1:
            renpy.show("dice 1", at_list=[truecenter])
        if dice_num == 2:
            renpy.show("dice 2", at_list=[truecenter])
        if dice_num == 3:
            renpy.show("dice 3", at_list=[truecenter])
        if dice_num == 4:
            renpy.show("dice 4", at_list=[truecenter])
        if dice_num == 5:
            renpy.show("dice 5", at_list=[truecenter])
        if dice_num == 6:
            renpy.show("dice 6", at_list=[truecenter])
        renpy.play("audio/diceroll.mp3")
        renpy.say(None, "Salió " + str(dice_num) + ".")
        renpy.hide("dice")
        return dice_num
    
    def movement(current, diceroll):
        global fullboard
        new = (fullboard.index(current) + diceroll)
        if new > 31:
            new = new % 32
        renpy.call(fullboard[new])
    
    def minigame(diff):
        global score
        global tickets
        diff_esp = {
            "easy": "fácil",
            "medium": "media",
            "hard": "difícil"
        }.get(diff)
        renpy.say(None, "Toca un ejercicio de dificultad " + diff_esp + ".")
        renpy.hide("dice")
        if diff == "easy":
            minigame_pool = ["math_incisos(\"easy\")", "verbal_incisos()"]
        elif diff == "medium":
            minigame_pool = ["math_incisos(\"medium\")", "verbal_incisos()", "verbal_lectura()"]
        elif diff == "hard":
            minigame_pool = ["math_incisos(\"hard\")", "verbal_incisos()",  "verbal_lectura()"]
        exec("global answer; answer = " + random.choice(minigame_pool))
        if answer == False:
            if tickets == True:
                tickets = False
                renpy.say(None, "Te equivocaste, pero por suerte tenías un ticket. No perderás puntos.")
            else:
                renpy.say(None, "Te equivocaste...")
                score = score - 1
        else:
            renpy.say(None, "¡Correcto!")
            score = score + 1
        renpy.say(None, "Puntaje actual: " + str(score))
    
    def passticket():
        global tickets
        if tickets == False:
            renpy.call("show_tickets")
        else:
            renpy.say(None, "Solo puedes tener un ticket a la vez.")
        
