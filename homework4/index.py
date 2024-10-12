list = []

while True:
    userInput = input("Введите число или end: ")

    if (userInput == 'end'):
        evens = []
        odds = []

        for num in list:
            if (num % 2 == 1):
                odds.append(num)
            else:
                evens.append(num)

        print(f'Четные числа: {evens}')
        print(f'Нечетные числа: {odds}')

        break

    else:
        try:
            list.append(int(userInput))
        except:
            print("Значение не было добавлено в общий список") 