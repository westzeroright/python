from stack import Stack

s = Stack()
parseq = input("괄호 입력 ; ")
for p in parseq:
    if p == '(': s.push(p)
    elif p == ')': s.pop()
    else: print("Not allowed Symbol")
if len(s) > 0: print("False")
else: print("True")
