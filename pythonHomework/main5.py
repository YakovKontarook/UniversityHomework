number = int(input("Введите целое число: "))
if number == 0:
    result = "ноль"
elif number > 0:
    result = "положительное"
else:
    result = "отрицательное"

if number % 2 == 0:
    result += " четное число"
else:
    result += " нечетное число"

print(result)

