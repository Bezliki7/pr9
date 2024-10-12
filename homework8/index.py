import random

ticket = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]

userNumbers = []
selectedRows = set()  

print("Билеты:")
for row in ticket:
    print(row)

while len(userNumbers) < 5:  
    try:
        num = int(input(f"Выберите число билета: "))
        
        if any(num in row for row in ticket):
            rowIndex = next(i for i, row in enumerate(ticket) if num in row)

            if rowIndex in selectedRows:
                print("Вы уже выбрали число из этого ряда. Выберите другое число.")
                continue 

            userNumbers.append(num)
            selectedRows.add(rowIndex)
        else:
            print("Некорректный ввод. Выберите число из билета.")
    except:
        print("Некорректный ввод. Выберите число из билета.")

random_numbers = random.sample([num for row in ticket for num in row], 5)

print(f"Ваши числа: {userNumbers}")
print(f"Случайно выбранные числа: {random_numbers}")

