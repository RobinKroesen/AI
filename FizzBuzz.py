for i in range(100):
    getal = i+1
    if getal%3 == 0:
        if getal%5 == 0:
            getal = "FizzBuzz"
        else:
            getal = "Fizz"
    elif getal%5 == 0:
        if getal%3 == 0:
            getal = "FizzBuzz"
        else:
            getal = "Buzz"
    print(getal)

