def ArrayMax(A,n):
    currentMax = A[0]
    for i in range(1,n):
        if currentMax < A[i]:
            currentMax = A[i]
    return currentMax

def sum1(A,n):
    sum = 0
    for i in range(1,n):
        if A[i] % 2 == 0:
            sum += A[i]
    return sum

def sum2(A,n):
    sum = 0
    for i in range(1,n):
        for j in range(1,n):
            sum += A[i] * A[j]
    return sum

def increment_one(a):
    return a+1

def number_of_bits(n):
    count = 0
    while n > 0:
        n = n // 2
        cout += 1
    return count
