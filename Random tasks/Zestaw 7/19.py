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

def usunDuplikaty(p):
    if p is None or p.next is None:
        return 0

    w = Node(None)
    w.next = p
    prev = w
    cnt = 0

    while True:
        num = p.val
        prev = p
        p = p.next
        if p is None:
            return (w.next, cnt)

        if p.val == num:
            while p is not None and p.val == num:
                cnt += 1
                p = p.next

            if p is None:
                prev.next = None
                return (w.next, cnt)

            prev.next = p
  

t = [1,1,1,2,2,3,4,5,5]
p = arrToList(t)
printList(p)
res = usunDuplikaty(p)
printList(res[0])
print(res[1])

