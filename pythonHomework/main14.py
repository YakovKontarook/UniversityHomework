N = int(input())
numbers = list(map(int, input().split()))
modified_array = [numbers[-1]] + numbers[:-1]
for number in modified_array:
    print(number, end=" ")


