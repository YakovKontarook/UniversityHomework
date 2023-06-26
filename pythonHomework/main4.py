number = input("Введите пятизначное число: ")
digits = list(map(int, number))
result = digits[1] ** digits[4] * digits[2] / (digits[0] - digits[3])
print(result)
