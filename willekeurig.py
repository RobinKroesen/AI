import random


def getal_raden():
    random.seed(5)
    getal = random.randint(1, 10)
    vraag = input("Raad het getal tussen 1 en 10: ")
    if int(vraag) == getal:
        return "Goed gedaan!"
    else:
        print("Probeer het nog een keer")
        return getal_raden()

print(getal_raden())