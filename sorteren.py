lst = [2, 463, 6, 1, 6745,2543,654,234,653,1093,32]

def gesorteerd(lst):
    while True:
        sorteerstatus = 0
        for item in range(len(lst) - 1):
            if lst[item] > lst[item + 1]:
                lst[item], lst[item + 1] = lst[item + 1], lst[item]
                sorteerstatus += 1
        if sorteerstatus == 0:
            return lst

print(gesorteerd(lst))