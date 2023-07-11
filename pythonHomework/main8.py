N = int(input("Введите число N: "))
count_zero = 0
for _ in range(N):
    num = int(input("Введите целое число: "))
    if num == 0:
        count_zero += 1

print(f"Количество чисел, равных нулю: {count_zero}")

