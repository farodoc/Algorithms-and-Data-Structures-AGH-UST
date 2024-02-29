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

def more1than2(num):
    cnt1 = 0
    cnt2 = 0

    while num > 0:
        if num % 3 == 1:
            cnt1 += 1

        elif num % 3 == 2:
            cnt2 += 1

        num //= 3

    return cnt1 > cnt2

def erase(p):
    if p is None:
        return p

    w = Node(None)
    w.next = p

    prev = w

    while p is not None:
        if more1than2(p.val):
            if p.next is None:
                prev.next = None
                return w.next

            prev.next = p.next
            p = p.next
            continue

        prev = p
        p = p.next

    return w.next

t = [1,2,3,4]
p = arrToList(t)
printList(p)
w = erase(p)
printList(w)
