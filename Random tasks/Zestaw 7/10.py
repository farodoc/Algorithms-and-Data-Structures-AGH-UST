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

def listLen(p):
    w = p
    res = 0
    while w is not None:
        w = w.next
        res += 1
    
    return res

def reverse(p):
    if p is None:
        return p

    prev = None
    curr = p
    next = p.next

    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev

def addLists(p1, p2):
    if p1 is None:
        return p2

    elif p2 is None:
        return p1
    
    x = Node(None)
    w = x

    p1 = reverse(p1)
    p2 = reverse(p2)
    zapas = 0

    while p1 is not None and p2 is not None:
        num = p1.val + p2.val + zapas

        if num < 10:
            g = Node(p1.val + p2.val)
            w.next = g
            zapas = 0

        else:
            zapas = 1
            g = Node(num - 10)
            w.next = g

        w = w.next
        p1 = p1.next
        p2 = p2.next

    if p1 is None:
        if zapas == 0:
            w.next = p2
        
        else:
            while p2 is not None:
                num = p2.val + zapas
                if num < 10:
                    g = Node(num)
                    zapas = 0
                    w.next = g
                    w = w.next
                    p2 = p2.next
            
                else:
                    g = Node(0)
                    w.next = g
                    w = w.next
                    p2 = p2.next
            
            if zapas == 1:
                g = Node(1)
                w.next = g

    if p2 is None:
        if zapas == 0:
            w.next = p1
        
        else:
            while p1 is not None:
                num = p1.val + zapas
                if num < 10:
                    g = Node(num)
                    zapas = 0
                    w.next = g
                    w = w.next
                    p1 = p1.next
            
                else:
                    g = Node(0)
                    w.next = g
                    w = w.next
                    p1 = p1.next
            
            if zapas == 1:
                g = Node(1)
                w.next = g

    w = reverse(x.next)
    return w

t1 = [9,9]
t2 = [1,5]
p1 = arrToList(t1)
p2 = arrToList(t2)

w = addLists(p1, p2)

printList(w)