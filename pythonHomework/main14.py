N = int(input())
numbers = list(map(int, input().split()))
for i in range(N // 2):
    temp = numbers[i]
    numbers[i] = numbers[N - i - 1]
    numbers[N - i - 1] = temp
    
for number in numbers:
    print(number)


