import random

randomNumbers = [random.randint(1, 100) for _ in range(10)]

print(f'Исходные данные: {randomNumbers}')

min, max = min(randomNumbers), max(randomNumbers)

minIndex, maxIndex = randomNumbers.index(min), randomNumbers.index(max)

randomNumbers[minIndex] = max
randomNumbers[maxIndex] = min

print(f'мин: {min}, макс: {max}')
print(f'Измененный лист: {randomNumbers}')