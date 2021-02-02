tekst = input("Geef een tekst: ")
tekst_lijst = list(tekst)
encyptie_stappen = input("Geef een rotatie: ")
nieuwe_tekst = ""
for i in tekst_lijst:
    unicode_index = ord(i)
    nieuwe_letter = chr(unicode_index + int(encyptie_stappen))
    nieuwe_tekst += nieuwe_letter

print(f"Tekst in Ceasar letters: {nieuwe_tekst}")
