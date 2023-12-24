print("취존이 어떤 문장의 줄일말인가요?")
a = input()
a = a.replace(" ", "")
A = "취향 존중"
A = A.replace(" ", "")
if a == A:
    print("정답")
else:
    print("오답")
print('\n')

print("솔까말이 어떤 문장의 줄임말인가요?")
b = input()
b = b.replace(" ", "")
B = "솔직히 까놓고 말해서"
B = B.replace(" ", "")
if b == B:
    print("정답")
else:
    print("오답")
print('\n')

print("케바케가 어떤 문장의 줄임말인가요?")
c = input()
c = c.replace(" ", "")
C = "케이스 바이 케이스"
C = C.replace(" ", "")
if c == C:
    print("정답")
else:
    print("오답")
print('\n')

if a == A and b == B and c == C:
    print("3개 퀴즈 중 3개 정답")
elif (a == A and b != B and c != C) or (a != A and b == B and c != C) or (a != A and b != B and c == C):
    print("3개 퀴즈 중 1개 정답")
elif (a == A and b == B and c != C) or (a == A and b != B and c == C) or (a != A and b == B and c == C):
    print("3개 퀴즈 중 2개 정답")
else:
    print("3개 퀴즈 중 0개 정답")


