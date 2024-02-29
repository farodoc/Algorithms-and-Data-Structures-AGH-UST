from collections import deque

def messages(G, s):
    n = len(G)
    q = deque()
    visited = [False] * n
    visited[s] = True

    max_people = max_day = 0
    day = 1
    prev_people = 1
    q.append(s)

    while q:
        people_cnt = 0
        for _ in range(prev_people):
            u = q.popleft()
            for v in G[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
                    people_cnt += 1
        
        if people_cnt > max_people:
            max_people = people_cnt
            max_day = day
        
        prev_people = people_cnt
        day += 1

    return max_day, max_people

graph = [[1, 2], [0, 3, 4], [0, 5, 6], [1, 10], [1, 5, 7, 8, 7, 9, 11],
         [2, 4, 6], [2, 5], [4], [4], [4], [3], [4]]

print(messages(graph, 0))