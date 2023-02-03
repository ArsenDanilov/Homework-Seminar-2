import math
# - 6782 -> 23
# - 0,56 -> 11



number = (input('Введите число: '))
symbols_value = (len(number))
number = float(number)
sum = 0

if number < 1:
    for i in range (symbols_value):
        number *= 10

while number > 0:
    sum = sum + number % 10
    number = number // 10
print(int(sum))


