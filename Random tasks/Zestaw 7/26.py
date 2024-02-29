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

def contains(p1, p2):
    if p1 is None or p2 is None:
        return True
    
    len1 = 1
    p = p1
    while p is not None:
        p = p.next
        len1 += 1

    len2 = 1
    p = p2
    while p is not None:
        p = p.next
        len2 += 1

    if len1 > len2:
        while p1 is not None and p1.val != p2.val:
            p1 = p1.next

        if p1 is None:
            return False

        while p1 is not None and p2 is not None and p1.val == p2.val:
            p1 = p1.next
            p2 = p2.next

        if p2 is None:
            return True
        
        else:
            return False

    else:
        while p2 is not None and p2.val != p1.val:
            p2 = p2.next

        if p2 is None:
            return False

        while p1 is not None and p2 is not None and p1.val == p2.val:
            p1 = p1.next
            p2 = p2.next

        if p1 is None:
            return True
        
        else:
            return False

t1 = [2,3,5,7,11,13]
t2 = [7, 5]
p1 = arrToList(t1)
p2 = arrToList(t2)
printList(p1)
printList(p2)
print(contains(p1,p2))