class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def printAll(p):
    if p is not None:
        print(p.val)
        printAll(p.next)
        
def findNum(p, num):
    while p is not None:
        if p.val == num:
            return True
        
        p = p.next

    return False

def member(val, p):
    while p is not None and p.val < val:
        p = p.next

    return p is not None and p.val == val

a = Node(1)
b = Node(2)
c = Node(7)

a.next = b
b.next = c

print(findNum(a, 2))