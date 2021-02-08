import random

kleuren = ['A', 'B', 'C', 'D', 'E', 'F']

def antwoord_genereren():
    gegenereerde_combinatie_lijst = []
    random.seed(9)
    for i in range(4):
        gegenereerde_combinatie_lijst.append(random.choice(kleuren))
        gegenereerde_combinatie = ''.join(gegenereerde_combinatie_lijst)
    return gegenereerde_combinatie_lijst

def vraag_stellen():
    aantal_errors = 0
    combinatie_raden = input("raad een combinatie: ")
    if len(combinatie_raden) != 4:
        print("combinatie moet 4 tekens lang zijn")
        aantal_errors += 1
    for i in combinatie_raden:
        if i in kleuren:
            continue
        else:
            print(f"{i} is geen geldig teken (de geldige tekens zijn: ABCDEF)")
            aantal_errors += 1
    if aantal_errors > 0:
        return vraag_stellen()
    return combinatie_raden

def feedback(vraag, antwoord):
    index = 0
    feedback = [0, 0]
    for i in vraag:
        status = 0
        if i in antwoord:
            feedback[0] += 1
            status += 1
            if i == antwoord[index]:
                feedback[1] += 1
                feedback[0] -= 1
                status += 1
        if status > 0:
            index_2 = 0
            for j in antwoord:
                if i == j:
                    antwoord[index_2] = ' '
                    break
                index_2 += 1
        index += 1
    return feedback

def speler_tegen_computer(vraag, antwoord):
        return feedback(vraag, antwoord)

for i in range(10):
    if print(speler_tegen_computer(vraag_stellen(), antwoord_genereren())) == [0,4]:
        print("Goed geraden")
        break
    if i == 9:
        print("Helaas pindakaas")