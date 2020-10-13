################################################################################
## Ejercicios de memoria
################################################################################

init offset = -10

init python:
    renpy.image("row1", HBox("memory/memoryback.jpg", "memory/memoryback.jpg", "memory/memoryback.jpg", "memory/memoryback.jpg", spacing = 100))
    renpy.image("row2", HBox("memory/memoryback.jpg", "memory/memoryback.jpg", "memory/memoryback.jpg", "memory/memoryback.jpg", spacing = 100))
    renpy.image("row3", HBox("memory/memoryback.jpg", "memory/memoryback.jpg", "memory/memoryback.jpg", "memory/memoryback.jpg", spacing = 100))
    renpy.image("memorygame", VBox("row1", "row2", "row3", spacing = 100))
    class Card:
        def __init__(self, value, image):
            self.value = value
            self.image = image
            self.back = "memoryback"
    
    def memorySetUp():
        import random
        random.seed()
        Drag("row1")
        renpy.show("memorygame", at_list=[Transform(zoom = 0.25), truecenter])
        

