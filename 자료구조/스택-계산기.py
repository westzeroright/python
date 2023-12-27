from stack import Stack

expr = input("수식을 입력하세요 : ")

def get_token_list(expr):
    numbers = list('0123456789.')
    token_list = []

    i = 0
    while i < len(expr):
        j = 1
        if expr[i] in numbers:
            while i + j < len(expr):
                if expr[i+j] in numbers:
                    j += 1
                else:
                    break
            token_list.append(float((''.join(expr[i:i+j]))))
            i += j
        else:
            token_list.append(expr[i])
            i += 1
    return token_list

def get_token_list2(expr):
    tokens = []
    current_token = ''
    numbers = '123456789.'
    operators = ['+','-','*','/']

    for char in expr:
        if char in numbers:
            current_token += char
        elif char in operators:
            if current_token:
                tokens.append(float(current_token))
                current_token = ''
            tokens.append(char)
        elif char == ' ':
            pass
        else:
            print("예외처리")

    if current_token:
        tokens.append(float(current_token))

    return tokens

priority = {'(': 1, ')': 1, '+': 2, '-': 2, '*': 3, '/': 3}
def infix_to_postfix(token_list):
    opstack = Stack()
    outstack = []

    for token in token_list:
        if token == '(':
            opstack.push(token)
        if token == ')':
            while opstack.top() != '(':
                outstack.append(opstack.pop())
            opstack.pop()
        if token in priority:
            while opstack:
                if priority[opstack.top()] >= priority[token]:
                    outstack.append(opstack.pop())
                else:
                    break
            opstack.push(token)
        else: # if token == operand:
            outstack.append(token)
    while opstack:
        outstack.append(opstack.pop())

    return outstack
            
def compute_postfix(token_list):
    s = Stack()
    operators = ['+','-','*','/']

    for token in token_list:
        if token in operators:
            a = s.pop()
            b = s.pop()
            if token == '+':
                s.push(a + b)
            if token == '-':
                s.push(a - b)
            if token == '*':
                s.push(a * b)
            if token == '/':
                s.push(a / b)
        else: # if token == operand
            s.push(float(token))

    return s.pop()

        
token_list = get_token_list(expr)
token_list = infix_to_postfix(token_list)
result = compute_postfix(token_list)

print("=", result)
