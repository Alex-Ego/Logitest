################################################################################
## Ejercicios de matemáticas
################################################################################

init offset = -1

init python:
    import codecs
    import random
    def math_exe(tema):
        with renpy.file("minigames/math/" + tema + ".txt") as f:
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
        print(exercise)
        option_prompt = zip(exercise[1], exercise[2])
        print(option_prompt)
        
        narrator(exercise[0], interact=False)
        ans = renpy.display_menu(option_prompt)
        if ans == "1":
            narrator("¡Correcto!")
        else:
            narrator("Buuuuuuuu...")

