import random

randomNumbers = [random.randint(1, 100) for _ in range(10)]

print(f'Исходные данные: {randomNumbers}')

randomNumbersLen = len(randomNumbers) -1

list = [randomNumbers[index] for index in range(0, randomNumbersLen) 
        if (randomNumbers[index] > randomNumbers[index-1] or index == 0)]
print(f'Все элементы списка, которые больше предыдущего элемента: {list}')