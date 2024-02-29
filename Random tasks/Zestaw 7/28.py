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

def eraseDuplicates(p1, p2):
    if p1 is None or p2 is None:
        return 0

    w = Node(None)
    w.next = p2
    cnt = 0

    while p1 is not None:
        num = p1.val
        g = p2
        prev = w

        while g is not None:
            if g.val == num:
                prev.next = g.next
                g = g.next
                prev = g
                cnt += 1
        
            else:
                prev = g
                g = g.next

        p1 = p1.next

    return cnt

t1 = [2,3,5,7,11,13,17]
t2 = [13]
p1 = arrToList(t1)
p2 = arrToList(t2)
printList(p1)
printList(p2)
print(eraseDuplicates(p1,p2))