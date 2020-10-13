################################################################################
## Funciones (a la mala, yikes)
################################################################################

init -5 python:
    import random
    
    def diceRoll():
        renpy.play("audio/diceshake.mp3")
        renpy.say(None, "Tirando el dado...")
        random.seed()
        dice_num = random.randint(1, 6)
        print(dice_num)
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
        return dice_num
    
    def movement(current, diceroll):
        fullboard = ["inicio", "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "c11", "c12", "c13", "c14", "c15", "c16", "c17", "c18", "c19", "c20", "c21", "c22", "c23", "c24", "c25", "c26", "c27", "c28", "c29", "c30", "c31"]
        print(current)
        new = (fullboard.index(current) + diceroll)
        if new > 31:
            new = new % 32
        print(new)
        print(fullboard[new])
        renpy.call(fullboard[new])
        renpy.hide("dice")
        
