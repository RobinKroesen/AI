import random

kleuren = ['A', 'B', 'C', 'D', 'E', 'F']

def jij_raad():
    #Het raden van de combinatie.
    #De speler mag 10 keer kiezen dus 10 keer herhalen
    for i in range(10):
        # het genereren van een combinatie dat de speler gaat proberen te raden
        gegenereerde_combinatie_lijst = []
        random.seed(9)
        for i in range(4):
            gegenereerde_combinatie_lijst.append(random.choice(kleuren))
            gegenereerde_combinatie = ''.join(gegenereerde_combinatie_lijst)
        print(gegenereerde_combinatie)

        #Controleren van de ingevoerde combinatie op lengte en gebruikte tekens
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
                combinatie_raden = input("raad een combinatie: ")

        #Als de geraden combinatie klopt
        if combinatie_raden == gegenereerde_combinatie:
            return print("geraden!")

        #feedback geven
        index = 0
        feedback = [0, 0]
        for i in combinatie_raden:
            status = 0
            if i in gegenereerde_combinatie_lijst:
                feedback[0] += 1
                status += 1
                if i == gegenereerde_combinatie[index]:
                    feedback[1] += 1
                    feedback[0] -= 1
                    status += 1
            if status > 0:
                index_2 = 0
                for j in gegenereerde_combinatie:
                    if i == j:
                        gegenereerde_combinatie_lijst[index_2] = ' '
                        break
                    index_2 += 1
            index += 1
        print(feedback)
    print(f"Helaas, code is niet gekraakt. De code was {gegenereerde_combinatie}")


def gamemode_kiezen():
    gamemode = input("Typ 0 voor zelf raden en 1 om de computer te laten raden: ")
    if gamemode == '0':
        return jij_raad()
    elif gamemode == '1':
        return computer_raad()
    else:
        print("Kies een geldige gamemode")
        return gamemode_kiezen()


jij_raad()