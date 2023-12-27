import random

def updown(answer, num):
    if answer > num:
        return "업"
    elif answer < num:
        return "다운"
    else:
        return "정답"

target = random.randint(1,20)
chance = 0

while chance < 3:
    number = int(input("숫자를 맞춰보세요 : "))
    result = updown(target, number)
    print(result)

    if result == "정답":
        break

    chance += 1

if result != "정답":
    print("실패")
