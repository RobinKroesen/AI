#string in string

def string_in_string():
    invoer_1 = input("Geef een string: ")
    invoer_2 = input("Geef nog een string: ")

    for i in range(len(invoer_2)):
        if invoer_2[i] != invoer_1[i]:
            print(f"Het eerste verschil zit op index {i}")
            return

string_in_string()