################################################################################
## Inicialización
################################################################################

## La sentencia 'init offset' da preferencia a las sentencias de inicialización
## de este archivo respecto a otros archivos.
init offset = -2

init python:
    
    def pos1(trans, st, at):
        trans.xpos = 600
        trans.ypos = 480
        
    def pos2(trans, st, at):
        trans.xpos = 775
        trans.ypos = 506
        trans.yoffset = -60
    
    def pos3(trans, st, at):
        trans.xpos = 942
        trans.ypos = 505
        trans.yoffset = -60
    
    def pos4(trans, st, at):
        trans.xpos = 1107
        trans.ypos = 393
        trans.yoffset = -60
    
    def pos5(trans, st, at):
        trans.xpos = 1109
        trans.ypos = 261
        trans.yoffset = -60