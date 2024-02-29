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

def removeLongest(p):
    if p is None or p.next is None:
        return p

    w = Node(None)
    w.next = p
    prev = w
    longest = 0
    startLongest = None
    endLongest = None
    flag = False

    while p is not None:
        if p.next is not None:
            if p.next.val > p.val:
                cnt = 1
                currStart = prev
                currEnd = p.next
                currPrev = p

                while currEnd is not None and currEnd.val > currPrev.val:
                    currPrev = currEnd
                    currEnd = currEnd.next
                    cnt += 1

                if cnt > longest:
                    startLongest = currStart
                    endLongest = currEnd
                    longest = cnt
                    flag = True

                elif cnt == longest:
                    flag = False

        prev = p
        p = p.next

    if flag:
        startLongest.next = endLongest

    return w.next

t = [1,2,3,2,3,4,6,1,2]
p = arrToList(t)
printList(p)
w = removeLongest(p)
printList(w)

                

