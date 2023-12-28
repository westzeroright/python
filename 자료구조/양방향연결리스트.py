# head 노드는 항상 dummy 노드
class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = self.prev = self

    def __str__(self):
        return str(self.key)

class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.size = 0

    def __iter__(self):
        v = self.head
        while v != self.head:
            yield v
            v = v.next

    def __str__(self):
            return "".join(str(v.key) for v in self)

    def __len__(self):
        return self.size

    def splice(self, a, b, x):
        if a == None or b == None or x == None:
            return
        ap = a.prev
        bn = b.next
        xn = x.next

        # CUT [a..b]
        ap.next = bn
        bn.prev = ap

        # PASTE [a..b] after x
        xn.prev = b
        b.next = xn
        a.prev = x
        x.next = a

    def moveAfter(self, a, x):
        self.splic(a, a, x)

    def moveBefore(self, a, x):
        self.splice(a, a, x.prev)

    def insertAfter(self, x, key):
        self.moveAfter(Node(key), x)

    def insertBefore(self, x, key):
        self.moveBefor(Node(key), x)

    def pushFront(self, key):
        self.insertAfter(self.head, key)

    def pushBack(self, key):
        self.insertBefore(self.head, key)

    def search(self, key):
        v = self.head
        while v.next != self.head:
            if v.key == key:
                return v
            v = v.next
        return None

    def remove(x):
        if x == None or x == self.head:
            return
        x.prev.next = x.next
        x.next.prev = x.prev
        del x

    def popFront(self):
        if self.isEmpty():
            return None
        key = self.head.next.key
        self.remove(self.head.next)
        return key

    def popBack(self):
        if self.isEmpty():
            return None
        key = self.head.prev.key
        self.remove(self.head.prev)
        return key

    # 기타 연산 : join, split
    
        
