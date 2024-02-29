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

def insertSrtring(p, word):
    g = Node(word)
    if p is None:
        return (g, True)

    w = Node(None)
    w.next = p
    prev = w

    while p is not None and p.val < word:
        prev = p
        p = p.next

    if p is None:
        prev.next = g
        return (w.next, True)

    if p.val == word:
        return (w.next, False)

    prev.next = g
    g.next = p

    return (w.next, True)

t = ['ala','alo','elo']
p = arrToList(t)
printList(p)
res = insertSrtring(p, 'elooo')
w, moc = res[0], res[1]
printList(w)
print(moc)