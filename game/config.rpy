################################################################################
## Inicialización
################################################################################

## La sentencia 'init offset' da preferencia a las sentencias de inicialización
## de este archivo respecto a otros archivos.
init offset = -2

init python:
    
    def replace_text(s):
        s = s.replace('á', u'\u00E1')
        s = s.replace('é', u'\u00E9')
        s = s.replace('í', u'\u00ED')
        s = s.replace('ó', u'\u00F3')
        s = s.replace('ú', u'\u00FA')
        s = s.replace('¿', u'\u00BF')
        return s
    
    config.replace_text = replace_text