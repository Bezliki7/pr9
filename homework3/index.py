list = []

while True:
    userInput = input("Введите число или end: ")

    if (userInput == 'end'):
        ans = [(number) for number in list if number % 2 == 1]

        if (len(ans)):
            print(f'Все введенные нечетные числа: {ans}')
        else:
            print("Нечетные числа осутствуют в списке")
        break

    else:
        try:
            list.append(int(userInput))
        except:
            print("Значение не было добавлено в общий список") 