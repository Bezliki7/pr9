try:
    a = float(input("Введите значение для a: "))
    b = float(input("Введите значение для b: "))

    intA, intB = int(a), int(b)
    listSqr = [n * n for n in range(intA, intB)]
    print(listSqr)
except ValueError:
    print('неверное значение')