class Node:
    def __init__(self,val):
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

def iloczyn(p1, p2):
    if p1 is None or p2 is None:
        return None

    x = Node(None)
    res = x

    while p1 is not None and p2 is not None:
        if p1.val < p2.val:
            p1 = p1.next

        elif p1.val > p2.val:
            p2 = p2.next

        else:
            x.next = p1
            x = x.next
            p1 = p1.next
            p2 = p2.next
            x.next = None

    return res.next

t1 = [1,2,2,4,5,7,8]
t2 = [0,2,3,5,8,8]

p1 = arrToList(t1)
p2 = arrToList(t2)

printList(p1)
printList(p2)

printList(iloczyn(p1,p2))