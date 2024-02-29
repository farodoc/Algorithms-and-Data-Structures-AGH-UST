from queue import PriorityQueue
from collections import deque

def train(T, m):
    q = PriorityQueue()

    for i in range(len(T)):
        q.put((T[i][0], 1))
        q.put((T[i][1], -1))

    cnt = 0

    while not q.empty():
        _, status = q.get()

        if status == 1:
            cnt += 1

        else:
            cnt -= 1

        if cnt > m:
            return False
        
    return True


def covid(T, k):
    n = len(T)
    cnt = 0
    prev = None
    zone = None

    for j in range(k - 1 , -1, -1):
        if T[j]:
            prev = j
            zone = j + k - 1
            cnt += 1
            break

    if prev is None:
        return -1
    
    i = zone + k

    while i < n:
        city_found = False
        for j in range(i, prev, - 1):
            if T[j]:
                if j == prev:
                    return -1
                
                prev = j
                zone = j + k - 1
                cnt += 1
                city_found = True
                break

        if city_found == False:
            return -1
        

        i = zone + k

    if zone < n - 1:
        for i in range(n - 1, prev, -1):
            if T[i]:
                return cnt + 1

    return cnt


def can_add(p1, p2):
    if p2[0] >= p1[1]:
        return True
    
    return False

def przedzialy(T, k):
    T.sort(key = lambda x:x[1])
    n = len(T)

    res = []
    min_len = float('inf')

    for i in range(n):
        cnt = 1
        prev = T[i]
        result = [T[i]]
        for j in range(i + 1, n):
            if cnt == k:
                leng = result[len(result) - 1][1] - result[0][0]
                if leng < min_len:
                    res = result
                    min_len = leng

            if can_add(prev, T[j]):
                cnt += 1
                prev = T[j]
                result.append(T[j])

    if min_len != float('inf'):
        return res

    return False


def smallest_word(s):
    n = len(s)
    cnt = [0] * 26
    v = [False] * 26
    q = deque()

    for c in s:
        cnt[ord(c) - 97] += 1

    q.append(s[0])
    cnt[ord(s[0]) - 97] -= 1
    v[ord(s[0]) - 97] = True

    for i in range(1, n):
        c = s[i]
        
        if v[ord(c) - 97]:
            cnt[ord(c) - 97] -= 1
            continue

        while q:
            stack_c = q.pop()
            if c < stack_c and cnt[ord(stack_c) - 97] > 0:
                v[ord(stack_c) - 97] = False
                q.append(c)
                v[ord(c) - 97] = True
                cnt[ord(c) - 97] -= 1
                break

            else:
                q.append(stack_c)
                q.append(c)
                v[ord(c) - 97] = True
                cnt[ord(c) - 97] -= 1
                break

    res = ""

    while q:
        c = q.popleft()
        res += c

    return res

s = "cbdaccbc"

print(smallest_word(s))