import random

randomNumbers = [random.randint(1, 100) for _ in range(10)]

print(f'Исходные данные: {randomNumbers}')

ans = list(randomNumbers)

for i in range(0, len(randomNumbers)):
    if (i == 0):
        ans[i] = randomNumbers[-1]
    else:
        ans[i] = randomNumbers[i-1]

print(f'Сдвинутый лист: {ans}')
