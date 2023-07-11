number = int(input("Введите пятизначное число: "))

units = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = (number // 1000) % 10
ten_thousands = (number // 10000) % 10

difference = ten_thousands - thousands
result = ((tens ** units) * hundreds) / difference if difference != 0 else float('nan')

print(f"Результат: {result}")
