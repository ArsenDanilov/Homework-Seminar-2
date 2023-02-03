n = int(input('Введите число: '))

list = [round((1 + 1 / i)**i, 2) for i in range (1, n+1)]


sum = 0

for i in range (n):
    sum += list[i]
    print(sum)
print()
print(float(sum))