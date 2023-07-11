X = int(input("Введите натуральное число X: "))

count = 0
for i in range(1, int(X ** 0.5) + 1):
    if X % i == 0:
        count += 1
        if X // i != i:
            count += 1

print(f"Количество натуральных делителей числа X: {count}")

