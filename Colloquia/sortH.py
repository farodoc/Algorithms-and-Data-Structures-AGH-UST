class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def heapify(t, i, n):
    l = 2 * i + 1
    r = 2 * i + 2
    min_idx = i

    if l < n and t[l].val < t[min_idx].val:
        min_idx = l

    if r < n and t[r].val < t[min_idx].val:
        min_idx = r

    if min_idx != i:
        t[i], t[min_idx] = t[min_idx], t[i]
        heapify(t, min_idx, n)

def sortH(p, k):
    k += 1
    g = Node(None)
    w = g
    heap = [0] * k

    for i in range(k):
        heap[i] = p
        p = p.next

    for i in range(k//2, -1, -1):
        heapify(heap, i, k)
    
    while p is not None:
        g.next = heap[0]
        g = g.next
        heap[0] = p
        p = p.next
        heapify(heap, 0, k)

    for i in range(k):
        g.next = heap[0]
        g = g.next
        heap[0] = Node(float('inf'))
        heapify(heap, 0, k)

    return w.next

a = Node(5)
b = Node(7)
c = Node(3)
d = Node(4)
e = Node(6)

a.next = b
b.next = c
c.next = d
d.next = e
w = a
for i in range(5):
    print(w.val)
    w = w.next

print("-----")

w = sortH(a, 3)
for i in range(5):
    print(w.val)
    w = w.next