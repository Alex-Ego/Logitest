################################################################################
## Ejercicios verbales
################################################################################

init offset = -10

init python:
    import codecs
    import random
    def verbal_incisos():
        global score
        with renpy.file("minigames/reading/verbal.txt") as f:
            lines = f.readlines()
            prompts = lines[0].strip().decode('utf-8').split(",")
            options = lines[1].strip().decode('utf-8').split(". ")
            answers = lines[2].strip().decode('utf-8').split(". ")
        exercise_list = list(zip(prompts, options, answers))
        random.seed()
        exercise = list(random.choice(exercise_list))
        print(exercise)
        exercise[1] = exercise[1].split(", ")
        exercise[2] = exercise[2].split(",")
        option_prompt = zip(exercise[1], exercise[2])
        
        
        narrator(exercise[0], interact=False)
        ans = renpy.display_menu(option_prompt)
        if ans == "1":
            return(True)
        else:
            return(False)
    
    def verbal_lectura():
        global score
        with renpy.file("minigames/reading/comprension.txt") as f:
            lines = f.readlines()
            prompts = lines[0].strip().decode('utf-8').split(". ")
            answers = lines[1].strip().decode('utf-8').split(". ")
            imgs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
            exercise_list = list(zip(prompts, answers, imgs))
        random.seed()
        exercise = list(random.choice(exercise_list))
        exercise[0] = exercise[0].split(", ")
        exercise[1] = exercise[1].split(", ")
        renpy.show("libro " + str(exercise[2]), at_list=[Position(xalign = 0.85, yalign = 0.5)])
        
        question = random.randrange(0, len(exercise[0]))
        ans = str(renpy.input(exercise[0][question] + " (No utilice acentos en su respuesta)"))
        ans = ans.strip()
        renpy.hide("libro " + str(exercise[2]))
        if ans.lower() == str(exercise[1][question]).lower():
            return(True)
        else:
            return(False)
        