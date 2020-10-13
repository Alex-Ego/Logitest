################################################################################
## Tablero
################################################################################

## La sentencia 'init offset' da preferencia a las sentencias de inicialización
## de este archivo respecto a otros archivos.
init offset = -5

label inicio:
    show peon 1:
        linear 0.2, function pos1

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
    