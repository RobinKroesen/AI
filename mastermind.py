import random
import itertools
import time

kleuren = ('A', 'B', 'C', 'D', 'E', 'F')
"""Lijst met de kleuren die gebruikt worden in het spel"""

def antwoord_genereren():
    """return een lijst met 4 willekeurige elementen uit kleuren"""

    gegenereerde_combinatie_lijst = []
    for i in range(4):
        gegenereerde_combinatie_lijst.append(random.choice(kleuren))
    return gegenereerde_combinatie_lijst

def vraag_stellen():
    """Vraag om een combinatie van 4 tekens aan de gebruiker,\n
        controleer of de combinatie de juiste lengte heeft en de juiste tekens bevat"""

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
    """return feedback over de gestelde vraag.\n
        Vergelijk de gestelde vraag met de geheime correcte combinatie(antwoord),\n
        return een lijst van 2 lang waarbij het eerste teken staat voor hoeveel tekens er op de goede plek staan\n
        en het tweede teken staat voor hoeveel tekens er in het antwoord staan maar niet op de juiste plek"""

    index = 0
    feedback = [0, 0]
    for i in vraag:
        status = 0
        if i in antwoord:
            feedback[1] += 1
            status += 1
            if i == antwoord[index]:
                feedback[0] += 1
                feedback[1] -= 1
                status += 1
        if status > 0:
            index_2 = 0
            for j in antwoord:
                if i == j:
                    antwoord[index_2] += '1'
                    break
                index_2 += 1
        index += 1
    return feedback


def speler_tegen_computer(antwoord):
    """Laat de speler 10 keer een vraag stellen.\n
        Geef na elke vraag feedback.\n
        Als de speler de geheime correcte combinatie(antwoord) juist geraden heeft is het spel afgelopen"""

    ronde_aantal = 0
    for i in range(10):
        print(f"U heeft nog {10 - ronde_aantal} rondes over")
        ronde_aantal += 1
        print(antwoord)
        vraag = vraag_stellen()
        uitkomst = feedback(vraag, antwoord)
        antwoord = ' '.join(antwoord).replace('1', '').split()
        if uitkomst == [4,0]:
            return (f"Gefeliciteerd u heeft de code gekraakt! in {ronde_aantal} rondes")
        if i == 9:
            return ("Helaas pindakaas")
        print(uitkomst)


def alle_combinaties():
    """"Maak een lijst met alle mogelijke combinaties"""

    alle_combis = sorted(list(set(itertools.combinations(kleuren * 4, 4))))
    return alle_combis


def a_simple_stratagy(alle_combis, antwoord):
    """"Een algoritme waarbij de computer vragen stelt op basis van feedback van de vorige vragen.\n
    bron: Yet another mastermind strategy, Barteld Kooi"""

    ronde_nummer = 0
    print(f"Het geheime antwoord is {antwoord}")
    for aantal_ronde in range(10):
        ronde_nummer += 1
        vraag = random.choice(alle_combis)
        print(f"De computer vraagt {vraag}")
        betere_lijst = []
        uitkomst = feedback(vraag, antwoord)
        antwoord = ' '.join(antwoord).replace('1', '').split()
        print(f"De feedback hier op is {uitkomst}")
        betere_lijst.clear()
        if uitkomst == [4,0]:
            print(f"Gefeliciteerd u heeft de code gekraakt, in {ronde_nummer} vragen")
            break
        for combi in alle_combis:
            combi = list(combi)
            teruggave = feedback(vraag, combi)
            combi = ' '.join(combi).replace('1', '').split()
            if teruggave == uitkomst:
                combi = tuple(combi)
                betere_lijst.append(combi)
        betere_lijst = list(set(betere_lijst))
        alle_combis.clear()
        for combi in betere_lijst:
            alle_combis.append(combi)
        time.sleep(1.5)


def combis_onderverdelen(alle_combis):
    """"Maak een dictionairy waarbij alle mogelijke combinaties zijn opgedeelt in AAAA, AAAB, ..."""

    AAAA = []
    AAAB = []
    AABB = []
    AABC = []
    ABCD = []
    gesoorteerde_combis = {}
    for combi in alle_combis:
        max_count = 0
        count_dict = {i:combi.count(i) for i in combi}
        if max(count_dict.values()) > max_count:
             max_count = max(count_dict.values())
        if max_count == 4:
            AAAA.append(combi)
        if max_count == 3:
            AAAB.append(combi)
        if max_count == 2 and len(count_dict) == 2:
            AABB.append(combi)
        if max_count == 2 and len(count_dict) != 2:
            AABC.append(combi)
        if max_count == 1:
            ABCD.append(combi)
    gesoorteerde_combis[f'AAAA'] = AAAA
    gesoorteerde_combis[f'AAAB'] = AAAB
    gesoorteerde_combis[f'AABB'] = AABB
    gesoorteerde_combis[f'AABC'] = AABC
    gesoorteerde_combis[f'ABCD'] = ABCD
    return gesoorteerde_combis


def worst_case(combis, keuze, antwoord):
    """"Een algoritme waarbij de computer kijkt naar de mogelijke antwoorden per catogorie(AAAA, AAAB...)
        en dan een vraag stelt uit de lijst met zo min mogelijk mogelijke antwoorden\n
        bron: Yet another mastermind strategy, Barteld Kooi"""

    ronde_nummer = 0
    print(f"Het geheime antwoord is {antwoord}")
    for ronde_aantal in range(10):
        ronde_nummer += 1
        hypothetische_mogelijke_uitkomsten = []
        vraag = random.choice(combis[keuze])
        print(F"De computer vraagt: {vraag}")
        terruggave = feedback(vraag, antwoord)
        antwoord = ' '.join(antwoord).replace('1', '').split()
        print(F"Feedback op deze vraag is {terruggave}")
        if terruggave == [4,0]:
            print(f"De code is gekraakt! in {ronde_nummer} pogingen")
            break
        for key in combis.values():
            for combi in key:
                combi = list(combi)
                uitkomst = feedback(vraag, combi)
                combi = ' '.join(combi).replace('1', '').split()
                if uitkomst == terruggave:
                    hypothetische_mogelijke_uitkomsten.append(combi)
        combis = combis_onderverdelen(hypothetische_mogelijke_uitkomsten)

        lengtes = []
        for key in combis:
            hoeveelheid_combis = len(combis[key])
            if hoeveelheid_combis > 0:
                lengtes.append(hoeveelheid_combis)
        for key in combis:
            if len(combis[key]) == min(lengtes):
                keuze = key
                break
        time.sleep(1.5)

def zelf_bedacht_algoritme(alle_combis, antwoord):
    """"Een algoritme waar eerst de kleuren die niet in het antwoord staan worden geëlimineerd
        en dan kijkt wanneer de feedback verbeterd om steeds een betere vraag te stellen"""

    vragen_die_ik_wil_stellen = [('A', 'A', 'A', 'A'), ('B', 'B', 'B', 'B'), ('C', 'C', 'C', 'C'), ('D', 'D', 'D', 'D'), ('E', 'E', 'E', 'E'), ('F', 'F', 'F', 'F')]
    mogelijke_antwoorden = []
    eerste_vragen_status = 0
    print(f"Het geheime antwoord is {antwoord}")
    for i in alle_combis:
        mogelijke_antwoorden.append(i)
    for aantal_rondes in range(100):
        vraag = random.choice(vragen_die_ik_wil_stellen)
        print(vraag)
        uitkomst = feedback(vraag, antwoord)
        antwoord = ' '.join(antwoord).replace('1', '').split()
        if uitkomst == [4,0]:
            print(f"De code is gekraakt! in {aantal_rondes} pogingen")
            break
        if uitkomst[0] == 0 and uitkomst[1] == 0:
            for combi in alle_combis:
                for letter in combi:
                    if vraag[0] == letter:
                        eliminate = letter
                        for mogelijke_combi in mogelijke_antwoorden:
                            if mogelijke_combi == combi:
                                mogelijke_antwoorden.remove(mogelijke_combi)
                                break
                        break
        vragen_die_ik_wil_stellen.remove(vraag)
        print(len(vragen_die_ik_wil_stellen))
        if uitkomst[0] == 3:
            eerste_vragen_status == 0
        if eerste_vragen_status == 0:
            if len(vragen_die_ik_wil_stellen) == 0:
                eerste_vragen_status += 1
                for i in mogelijke_antwoorden:
                    vragen_die_ik_wil_stellen.append(i)
        else:
            mogelijke_antwoorden.clear()
            for k in vragen_die_ik_wil_stellen:
                k = list(k)
                teruggave = feedback(vraag, k)
                k = ' '.join(k).replace('1', '').split()
                if teruggave[0] > uitkomst[0] or teruggave[1] > uitkomst[1]:
                    combi = tuple(combi)
                    mogelijke_antwoorden.append(combi)
        time.sleep(0.01)

def mastermind(alle_combis, antwoord):
    """"Laat de gebruiker kiezen tussen zelf spelen of de computer laten spelen. \n
        En bij laat de computer spelen de gebruiker kiezen uit de drie algoritmes"""
    q = input("Welke gamemode zou u willen spelen \nTyp 0 voor speler tegen computer \nTyp 1 voor computer tegen speler\ngamemode: ")
    mogelijke_q = ['0','1']
    mogelijke_q2 = ['0', '1', '2']
    if q not in mogelijke_q:
        print("\nkies een geldige gamemode\n")
        return gamemode_selecteren(alle_combis, antwoord)
    if q == '0':
        print(speler_tegen_computer(antwoord))
    if q == '1':
        q2 = input(f"\nVan welk algoritme gaat de computer gebruik maken?\nTyp 0 voor het simpele algoritme\nTyp 1 voor het 'Worst Case' algoritme\nTyp 2 voor het zelfgemaakte algoritme\nalgoritme: ")
        if q2 not in mogelijke_q2:
            print("\nkies een geldig algoritme\n")
        if q2 == '0':
            a_simple_stratagy(alle_combis, antwoord)
        if q2 == '1':
            worst_case((combis_onderverdelen(alle_combis)), 'AABB', antwoord)
        if q2 == '2':
            zelf_bedacht_algoritme(alle_combis, antwoord)

mastermind(alle_combinaties(), antwoord_genereren())