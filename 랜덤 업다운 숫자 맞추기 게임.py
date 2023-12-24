import random

target = random.randint(1, 20)

def updown(answer, num):
    if answer >= num:
        print("업")
    elif answer <= num:
        print("다운")
    else:
        print("정답")

chance = 0
number = int(input("숫자를 맞춰보세요 : "))
while (target != number):
    
    updown(target, number)
    chance +=1
    if chance > 2:
        print("실패")
        break
    number = int(input("숫자를 맞춰보세요 : "))
    if target == number:
        print("정답")

    
