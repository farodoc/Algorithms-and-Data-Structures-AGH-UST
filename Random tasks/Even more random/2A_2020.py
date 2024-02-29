class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def removeLongest(p):
    guard = Node(None)
    guard.next = p

    left = guard
    curr = p
    startLongest = None
    stopLongest = None
    lenCurr = 0
    lenLongest = 0

    if curr is None or curr.next is None:
        return 0

    while curr is not None:
        num = curr.val

        if curr.next is not None and curr.next.val == num:
            lenCurr = 2
            curr = curr.next

            while curr.next is not None and curr.next.val == num:
                lenCurr += 1
                curr = curr.next

            if lenCurr == lenLongest:
                startLongest = None
                stopLongest = None
                
            elif lenCurr > lenLongest:
                if curr.next is None:
                    startLongest = left
                    stopLongest = None
                
                else:
                    startLongest = left
                    stopLongest = curr.next

                lenLongest = lenCurr

        if curr.next is None:
            break

        left = curr
        curr = curr.next
    
    if startLongest is None and stopLongest is None:
        return 0
    
    startLongest.next = stopLongest
    if startLongest == guard:
        p.val = stopLongest.val
        p.next = stopLongest.next

    return lenLongest


def printList(p):
    while p.next is not None:
        print(p.val, end = ', ')
        p = p.next

    print(p.val)

a = Node(3)
b = Node(3)
c = Node(1)
d = Node(3)

a.next = b
b.next = c
c.next = d

printList(a)
print(removeLongest(a))
printList(a)
