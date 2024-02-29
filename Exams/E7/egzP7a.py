from egzP7atesty import runtests
from collections import deque
from math import inf

def akademik( T ):
    n = len(T)
    unmatched = []
    selected = [-1 for _ in range(n)]

    for source in range(n):
        if T[source][0] is None and T[source][1] is None and T[source][2] is None:
            continue

        notFound = True
        for target in T[source]:
            if target is not None and selected[target] == -1:
                selected[target] = source
                notFound = False
                break

        if notFound:
            unmatched.append(source)

    
    def DFS(source):
        for target in T[source]:
            if target is not None and not visited[target]:
                visited[target] = True

                if selected[target] == -1 or DFS(selected[target]):
                    selected[target] = source
                    return True
            
        return False
    
    for source in unmatched:
        visited = [False] * n
        DFS(source)

    
    cnt = 0
    no_preference = 0

    for i in range(n):
        if T[i][0] is None and T[i][1] is None and T[i][2] is None:
            no_preference += 1
            
        if selected[i] != -1:
            cnt += 1

    return n - cnt - no_preference

"""
def bfs(G, s, t, parent):
    n = len(G)
    visited = [False] * n
    q = deque()
    q.append(s)

    while q:
        v = q.popleft()

        for i in range(n):
            if G[v][i] != 0 and not visited[i]:
                parent[i] = v
                visited[i] = True
                q.append(i)
    
    return visited[t]

def ford_fulkerson(G, s, t):
    n = len(G)
    max_flow = 0
    parent = [None] * n

    while bfs(G, s, t, parent):
        curr_flow = inf
        v = t

        while v != s:
            curr_flow = min(curr_flow, G[parent[v]][v])
            v = parent[v]

        v = t

        while v != s:
            G[parent[v]][v] -= curr_flow
            G[v][parent[v]] += curr_flow
            v = parent[v]

        max_flow += curr_flow

    return max_flow


def akademik( T ):
    n=len(T)
    s = 2 * n
    t = 2 * n + 1

    ileNone=0
    for i in range(n):
        if T[i][0] is None:
            ileNone+=1

    matrix=[[0]*(2*n+2) for _ in range(2*n+2)]
    for i in range(n):
        matrix[s][i]=1
        matrix[n+i][t]=1
        for j in range(3):
            if T[i][j] is not None:
                matrix[i][n+T[i][j]]=1


    resCntr=ford_fulkerson(matrix, s, t)           

    
    return n-resCntr-ileNone"""

runtests ( akademik )