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

def unikaty(p):
    if p is None or p.next is None:
        return p

    w = Node(None)
    w.next = p
    prev = w 
    cnt = 0

    while True:
        x = 0
        while x < cnt and p is not None:
            prev = p
            p = p.next
            x += 1
        
        if p is None:
            break

        num = p.val
        prev = p
        p = p.next
        while p is not None:
            if p.val == num:
                prev.next = p.next
                p = p.next

            else:
                prev = p
                p = p.next

        p = w.next
        cnt += 1

    return w.next

t = [2,2,2,2,2]
p = arrToList(t)
printList(p)
w = unikaty(p)
printList(w)