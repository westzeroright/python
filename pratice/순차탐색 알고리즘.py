import random

key = int(input("key : "))

numbers = list(range(1, 50))
data = random.sample(numbers, 30)

def LineSearch(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i+1

value = LineSearch(30, key, data)

if value == None:
    print("존재하지 않습니다.")
else:
    print(f'{key}은(는) {value}번째에 있습니다.')

print(data)
