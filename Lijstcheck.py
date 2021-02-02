lst = [4,5,6,7,85,4,1,5,6,7,8,8,7,5,13]
lst1 = [0,1,0,1,1,0,1,1,1,0,0,1,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0]
def count(lst, x):
    freq_getal = 0
    for i in lst:
        if x == i:
            freq_getal += 1
    return freq_getal

def grootste_verschil(lst):
    max_verschil = 0
    index = 0

    while index < len(lst)-1:
        voorste_getal = lst[index]
        achterste_getal = lst[index + 1]
        if voorste_getal < achterste_getal:
            verschil = achterste_getal - voorste_getal
            if verschil > max_verschil:
                max_verschil = verschil
        elif voorste_getal == achterste_getal:
            verschil = 0
            if verschil > max_verschil:
                max_verschil = verschil
        else:
            verschil = voorste_getal - achterste_getal
            if verschil > max_verschil:
                max_verschil = verschil
        index += 1
    return f"Het grootste verschil tussen 2 opeenvolgende getallen is {max_verschil}"

def enen_en_nullen(lst1):
    freq0 = count(lst1, 0)
    freq1 = count(lst1, 1)
    if freq1 > freq0:
        if freq0 < 12:
            return True
    return False

print(enen_en_nullen(lst1))
print(grootste_verschil(lst))
print(f"het getal komt {count(lst, 5)} keer voor")

