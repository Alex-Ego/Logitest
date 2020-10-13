################################################################################
## Tablero
################################################################################

## La sentencia 'init offset' da preferencia a las sentencias de inicialización
## de este archivo respecto a otros archivos.
init offset = -4

label inicio:
    show peon 1:
        linear 0.2, function pos1
    $ current_pos = 0
    $ movement(fullboard[current_pos], diceRoll())
        
label c1:
    show peon 1:
        linear 0.2, function pos2
    $ current_pos = 1
    $ movement(fullboard[current_pos], diceRoll())
        
label c2:
    show peon 1:
        linear 0.2, function pos3
    $ current_pos = 2
    $ movement(fullboard[current_pos], diceRoll())

label c3:
    show peon 1:
        linear 0.2, function pos4
    $ current_pos = 3
    $ movement(fullboard[current_pos], diceRoll())

label c4:
    show peon 1:
        linear 0.2, function pos5
    $ current_pos = 4
    $ movement(fullboard[current_pos], diceRoll())

label c5:
    show peon 1:
        linear 0.2, function pos6
    $ current_pos = 5
    $ movement(fullboard[current_pos], diceRoll())

label c6:
    show peon 1:
        linear 0.2, function pos7
    $ current_pos = 6
    $ movement(fullboard[current_pos], diceRoll())

label c7:
    show peon 1:
        linear 0.2, function pos8
    $ current_pos = 7
    $ movement(fullboard[current_pos], diceRoll())

label c8:
    show peon 1:
        linear 0.2, function pos9
    $ current_pos = 8
    $ movement(fullboard[current_pos], diceRoll())

label c9:
    show peon 1:
        linear 0.2, function pos10
    $ current_pos = 9
    $ movement(fullboard[current_pos], diceRoll())

label c10:
    show peon 1:
        linear 0.2, function pos11
    $ current_pos = 10
    $ movement(fullboard[current_pos], diceRoll())

label c11:
    show peon 1:
        linear 0.2, function pos12
    $ current_pos = 11
    $ movement(fullboard[current_pos], diceRoll())

label c12:
    show peon 1:
        linear 0.2, function pos13
    $ current_pos = 12
    $ movement(fullboard[current_pos], diceRoll())

label c13:
    show peon 1:
        linear 0.2, function pos14
    $ current_pos = 13
    $ movement(fullboard[current_pos], diceRoll())

label c14:
    show peon 1:
        linear 0.2, function pos15
    $ current_pos = 14
    $ movement(fullboard[current_pos], diceRoll())

label c15:
    show peon 1:
        linear 0.2, function pos16
    $ current_pos = 15
    $ movement(fullboard[current_pos], diceRoll())

label c16:
    show peon 1:
        linear 0.2, function pos17
    $ current_pos = 16
    $ movement(fullboard[current_pos], diceRoll())

label c17:
    show peon 1:
        linear 0.2, function pos18
    $ current_pos = 17
    $ movement(fullboard[current_pos], diceRoll())

label c18:
    show peon 1:
        linear 0.2, function pos19
    $ current_pos = 18
    $ movement(fullboard[current_pos], diceRoll())

label c19:
    show peon 1:
        linear 0.2, function pos20
    $ current_pos = 19
    $ movement(fullboard[current_pos], diceRoll())

label c20:
    show peon 1:
        linear 0.2, function pos21
    $ current_pos = 20
    $ movement(fullboard[current_pos], diceRoll())

label c21:
    show peon 1:
        linear 0.2, function pos22
    $ current_pos = 21
    $ movement(fullboard[current_pos], diceRoll())

label c22:
    show peon 1:
        linear 0.2, function pos23
    $ current_pos = 22
    $ movement(fullboard[current_pos], diceRoll())

label c23:
    show peon 1:
        linear 0.2, function pos24
    $ current_pos = 23
    $ movement(fullboard[current_pos], diceRoll())

label c24:
    show peon 1:
        linear 0.2, function pos25
    $ current_pos = 24
    $ movement(fullboard[current_pos], diceRoll())

label c25:
    show peon 1:
        linear 0.2, function pos26
    $ current_pos = 25
    $ movement(fullboard[current_pos], diceRoll())

label c26:
    show peon 1:
        linear 0.2, function pos27
    $ current_pos = 26
    $ movement(fullboard[current_pos], diceRoll())

label c27:
    show peon 1:
        linear 0.2, function pos28
    $ current_pos = 27
    $ movement(fullboard[current_pos], diceRoll())

label c28:
    show peon 1:
        linear 0.2, function pos29
    $ current_pos = 28
    $ movement(fullboard[current_pos], diceRoll())

label c29:
    show peon 1:
        linear 0.2, function pos30
    $ current_pos = 29
    $ movement(fullboard[current_pos], diceRoll())

label c30:
    show peon 1:
        linear 0.2, function pos31
    $ current_pos = 30
    $ movement(fullboard[current_pos], diceRoll())

label c31:
    show peon 1:
        linear 0.2, function pos32
    $ current_pos = 31
    $ movement(fullboard[current_pos], diceRoll())


init python:
    
    ## Posiciones de todo el tablero
    
    def pos1(trans, st, at):
        trans.xpos = 1190
        trans.ypos = 615
        #Inicio
    
    def pos2(trans, st, at): 
        trans.xpos = 1190
        trans.ypos = 470
        #Verde
    
    def pos3(trans, st, at): 
        trans.xpos = 1190
        trans.ypos = 360
        #Amarillo
    
    def pos4(trans, st, at): 
        trans.xpos = 1190
        trans.ypos = 250
        #Rojo
    
    def pos5(trans, st, at): 
        trans.xpos = 1190
        trans.ypos = 140
        #Verde
    
    def pos6(trans, st, at): 
        trans.xpos = 1190
        trans.ypos = 30
        #Azul
    
    def pos7(trans, st, at): 
        trans.xpos = 1070
        trans.ypos = 30
        #Rojo
    
    def pos8(trans, st, at): 
        trans.xpos = 970
        trans.ypos = 30
        #Verde
    
    def pos9(trans, st, at):    
        trans.xpos = 860
        trans.ypos = 30
        #Azul
    
    def pos10(trans, st, at):    
        trans.xpos = 750
        trans.ypos = 30
        #Rojo
    
    def pos11(trans, st, at):    
        trans.xpos = 650
        trans.ypos = 30
        #Verde
    
    def pos12(trans, st, at):    
        trans.xpos = 550
        trans.ypos = 30
        #Amarillo
    
    def pos13(trans, st, at):    
        trans.xpos = 450
        trans.ypos = 30
        #Rojo
    
    def pos14(trans, st, at):    
        trans.xpos = 350
        trans.ypos = 30
        #Verde
    
    def pos15(trans, st, at):    
        trans.xpos = 250
        trans.ypos = 30
        #Amarillo
    
    def pos16(trans, st, at):    
        trans.xpos = 150
        trans.ypos = 30
        #Rojo
    
    def pos17(trans, st, at):    
        trans.xpos = 35
        trans.ypos = 30
        #Verde
    
    def pos18(trans, st, at):    
        trans.xpos = 35
        trans.ypos = 150
        #Azul
    
    def pos19(trans, st, at):    
        trans.xpos = 35
        trans.ypos = 250
        #Rojo
    
    def pos20(trans, st, at):    
        trans.xpos = 35
        trans.ypos = 360
        #Verde
    
    def pos21(trans, st, at):    
        trans.xpos = 35
        trans.ypos = 470
        #Amarillo
    
    def pos22(trans, st, at):    
        trans.xpos = 35
        trans.ypos = 615
        #Rojo
    
    def pos23(trans, st, at):    
        trans.xpos = 125
        trans.ypos = 615
        #Verde
    
    def pos24(trans, st, at):    
        trans.xpos = 230
        trans.ypos = 615
        #Amarillo
    
    def pos25(trans, st, at):    
        trans.xpos = 335
        trans.ypos = 615
        #Rojo
    
    def pos26(trans, st, at):    
        trans.xpos = 440
        trans.ypos = 615
        #Azul
    
    def pos27(trans, st, at):    
        trans.xpos = 545
        trans.ypos = 615
        #Amarillo
    
    def pos28(trans, st, at):    
        trans.xpos = 650
        trans.ypos = 615
        #Rojo
    
    def pos29(trans, st, at):    
        trans.xpos = 755
        trans.ypos = 615
        #Verde
    
    def pos30(trans, st, at):    
        trans.xpos = 860
        trans.ypos = 615
        #Rojo
    
    def pos31(trans, st, at):    
        trans.xpos = 965
        trans.ypos = 615
        #Amarillo
    
    def pos32(trans, st, at):    
        trans.xpos = 1070
        trans.ypos = 615
        #Rojo
    