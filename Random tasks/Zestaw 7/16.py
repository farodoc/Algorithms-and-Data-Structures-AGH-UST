class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def arrToList(t):
    x = Node(None)
    res = x
    n = len(t)

    for i in range(n):
        x.next = Node(t[i])
        x = x.next

    return res.next

def printList(p):
    while p.next is not None:
        print(p.val, end = ', ')
        p = p.next

    print(p.val)

def even5inOcta(num):
    cnt = 0

    while num > 0:
        if num % 8 == 5:
            cnt += 1

        num //= 8

    return cnt % 2 == 0


def moveEven(p):
    if p is None or p.next is None:
        return p

    w = Node(None)
    w.next = p
    
    prev = p
    p = p.next

    while p is not None:
        if even5inOcta(p.val):
            if p.next is None:
                prev.next = None
                p.next = w.next
                w.next = p
                return w.next

            prev.next = p.next
            p.next = w.next
            w.next = p
            p = prev.next

        else:
            prev = p
            p = p.next

    return w.next

t = [8,5,14]
p = arrToList(t)
printList(p)
w = moveEven(p)
printList(w)