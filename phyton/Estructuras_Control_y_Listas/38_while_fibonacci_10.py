anterior = 0
actual = 1
terminos = 0

while terminos < 10:
    print(anterior)
    anterior, actual = actual, anterior + actual
    terminos += 1
