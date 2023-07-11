N = int(input("Введите число N: "))

numbers = []
for _ in range(N):
    number = int(input("Введите число: "))
    numbers.append(number)

reversed_numbers = numbers[::-1]

for number in reversed_numbers:
    print(number)

