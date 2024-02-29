class Node:
    def __init__(self, value):
        self.value = value
        self.parent = self

def make_set(val):
    return Node(val)

def find(x):
    if x != x.parent:
        x.parent = find(x.parent)

    return x.parent

def union(x, y):
    x = find(x)
    y = find(y)

    if x.value == y.value:
        return
    
    if x.value < y.value:
        y.parent = x

    else:
        x.parent = y

def equivalent_letters(A, B, C):
    letters = []
    values = []

    for i in range(len(A)):
        if A[i] not in values:
            values.append(A[i])
            letters.append(make_set(A[i]))

        if B[i] not in values:
            values.append(B[i])
            letters.append(make_set(B[i]))


    for i in range(len(A)):
        a = letters[values.index(A[i])]
        b = letters[values.index(B[i])]

        union(a, b)


    new_word = ""
    for i in range(len(C)):
        if C[i] in values:
            x = find(letters[values.index(C[i])]).value
            new_word += x

        else:
            new_word += C[i]

    return new_word



A = "oauhihunosjrnhijsr"
B = "hozonbibieguiyuigb"
C = "abdfeiohiub"

print(equivalent_letters(A, B, C))