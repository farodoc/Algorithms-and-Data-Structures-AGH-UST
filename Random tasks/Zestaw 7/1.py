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

def member(p, num):
    if p is None:
        return False

    while p is not None and p.val < num:
        p = p.next

    if p is None or p.val > num:
        return False

    return True

def insert(p, num):
    w = Node(None)
    w.next = p
    prev = w

    while p is not None and p.val < num:
        prev = p
        p = p.next

    if p is not None and p.val == num:
        return w.next
    
    new = Node(num)
    new.next = p
    prev.next = new

    return w.next

def delete(p, num):
    w = Node(None)
    w.next = p
    prev = w

    if p is None:
        return w.next

    while p is not None and p.val < num:
        prev = p
        p = p.next

    if p is None or p.val > num:
        return w.next

    prev.next = p.next

    return w.next
    

    


t = [2,3,5,7,11]
p = arrToList(t)
printList(p)

p = delete(p,5)

printList(p)
