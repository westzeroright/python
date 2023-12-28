from Queue import Queue

def Josephus(n,k):
    Q = Queue()
    for i in range(1, n+1):
        Q.enqueue(i)

    last_person = None

    while len(Q) > 1:
        for j in range(k-1):
            Q.enqueue(Q.dequeue())

        Q.dequeue()

    return Q.dequeue()

print(Josephus(6,2))
