def fibonaci(getal1, getal2, n):
    n-=1
    if n == 0:
        return getal2
    return fibonaci(getal2, getal1+getal2, n)

print(fibonaci(0,1, 9))