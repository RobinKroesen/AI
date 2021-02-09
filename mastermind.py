#Hierboven staat de algemene feedback. Er staan ook nog comments bij individuele stukjes code voor specifiekere feedback.
#
#Het kan wel handig zijn om Docstrings aan je functies toe te voegen.
#Dit is een string in de eerste regel van een functie die (bijvoorbeeld) beschrijft wat de functie voor parameters heeft, wat die returned, en eventuele andere belangrijke details.
#
#Behalve een paar specifieke opmerking bij individuele functies zijn je functies en variabelenamen duidelijk.
#Je code lijkt te werken, en ik heb geen overduidelijke efficiëntieproblemen gezien.
#
#Wel zou ik voor jezelf zorgen dat je een goed plan hebt voor hoe je alles gaat ordenen wanneer de rest van de code geïmplementeerd word.
#Hoe sommige functies nu geïmplementeerd zijn vind ik het zelf moeilijk daar een beeld bij de krijgen, maar dat kan natuurlijk ook aan mij liggen.
#
#Je bent goed bezig, ga vooral door!




import random

kleuren = ['A', 'B', 'C', 'D', 'E', 'F'] #Het lijkt me dat je dit naar een Tuple kan veranderen omdat dit toch niet hoeft te veranderen tijdens het runnen van je code.


#het kan handig zijn je functies misschien wat duidelijkere namen te geven. 
#Ik kan lezen dat antwoord_genereren een willikeurige code genereert, maar zodra je bvb de bot gaat implementeren kan dit een verwarrende naam zijn.
def antwoord_genereren():
    gegenereerde_combinatie_lijst = []
    random.seed(9) #Wat is de bedoeling hiervan? Zo is de random generator toch niet meer random?
    for i in range(4):
        gegenereerde_combinatie_lijst.append(random.choice(kleuren))
        gegenereerde_combinatie = ''.join(gegenereerde_combinatie_lijst) #waarvoor creeer je dit variabele als je de lijst returned?
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
        return vraag_stellen() #leuk dat je dit recursief doet.
    return combinatie_raden 


#De feedback van je feedbackfunctie is omgekeerd van het formaat dat ze in de paper van de Universiteit Groningen hanteren.
#Word dat misschien verwarrend zodra je de bot schrijft?
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

#Heb je voor jezelf een duidelijk idee/plan hoe je het zo modulair en overzichtelijk mogelijk gaat aanpakken wanneer je de verschillende functies voor zowel de bot als het mens aan beide kanten van het spel gaat schrijven?
def speler_tegen_computer(vraag, antwoord):
        return feedback(vraag, antwoord)

for i in range(10):
    if print(speler_tegen_computer(vraag_stellen(), antwoord_genereren())) == [0,4]:
        print("Goed geraden")
        break
    if i == 9:
        print("Helaas pindakaas")
