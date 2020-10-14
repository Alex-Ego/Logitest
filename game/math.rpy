################################################################################
## Ejercicios de matemáticas
################################################################################

init offset = -10

init python:
    import codecs
    import random
    def math_incisos(level):
        global score
        tema = math_difficulty(level)
        with renpy.file("minigames/math/" + tema + ".txt") as f:
            lines = f.readlines()
            prompts = lines[0].strip().decode('utf-8').split(",")
            options = lines[1].strip().decode('utf-8').split(". ")
            answers = lines[2].strip().decode('utf-8').split(". ")
        if tema == "areas":
            imgs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            exercise_list = list(zip(prompts, options, answers, imgs))
        else:
            exercise_list = list(zip(prompts, options, answers))
        random.seed()
        exercise = list(random.choice(exercise_list))
        exercise[1] = exercise[1].split(", ")
        exercise[2] = exercise[2].split(",")
        if tema == "areas":
            renpy.show("area" + str(exercise[3]), at_list=[Position(xalign = 0.85, yalign = 0.5)])
        option_prompt = zip(exercise[1], exercise[2])
        
        
        narrator(exercise[0], interact=False)
        ans = renpy.display_menu(option_prompt)
        if tema == "areas":
            renpy.hide("area" + str(exercise[3]))
        if ans == "1":
            return(True)
        else:
            return(False)
    
    def math_difficulty(level):
        random.seed()
        if level == "easy":
            return((random.choice(["areas", "romanos"])))
        elif level == "medium":
            return(random.choice(["areas", "conversiones", "factorizacion", "romanos"]))
        else:
            return(random.choice(["conversiones", "factorizacion"]))

