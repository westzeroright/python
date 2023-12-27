import random

key = int(input("key : "))

def createData(): #중복, 이걸로 하면 발견한 첫번째 인덱스 반환
    data = []
    for i in range(30):
        num = random.randint(1, 50)
        data.append(num)
    return data

#중복x
numbers = list(range(1, 50))
num = random.sample(numbers, 30)

def binSearch(array, target, start, end):
    while target in array:
        mid = ( start + end ) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

data = sorted(createData())
num = sorted(num)

value = binSearch(num, key, 0, 29)

if value == None:
    print("존재하지 않습니다.")
else:
    print(f'{key}은(는) {value}번째에 있습니다.')

print(num)

          
