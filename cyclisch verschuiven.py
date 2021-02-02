def verschuiven(ch, n):
    ch_string = str(ch)
    ch_map = map(int, ch_string)
    ch_lijst = list(ch_map)
    if n > 0:
        for i in range(n):
            ch_lijst.append(ch_lijst[0])
            ch_lijst.remove(ch_lijst[0])
    elif n < 0:
        for i in range(int((n*n)**(1/2))):
            ch_lijst.insert(0,ch_lijst[len(ch_lijst)-1])
            ch_lijst.pop()
    omzetten_in_str = [str(ch_lijst) for ch_lijst in ch_lijst]
    verschoven_str = "".join(omzetten_in_str)
    return verschoven_str

print(verschuiven(1011000, 3))