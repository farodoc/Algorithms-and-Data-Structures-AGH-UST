# Given 2D array [N][N] in which each cell has the value "W" representing water or "L"
# representing land. Lake is a group of water cells connected by their banks. Assuming
# that array[0][0] and array[n-1][n-1] are land. Check if it is possible to go from
# [0][0] to [n-1][n-1] by land. You can only walk sideways not diagonally. Also find
# the shortest path between this cells.

from collections import deque

def bfs(G):
    n = len(G)
    q = deque()
    d = [[-1 for _ in range(n)] for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    parent = [[None for _ in range(n)] for _ in range(n)]

    q.append((0,0,0))

    while q:
        row, col, dist = q.popleft()
        visited[row][col] = True
        d[row][col] = dist

        if 0 <= row - 1 < n and 0 <= col < n and G[row - 1][col] == 'L' and not visited[row - 1][col]:
            parent[row - 1][col] = (row, col)
            q.append((row - 1, col, dist + 1))
        
        if 0 <= row + 1 < n and 0 <= col < n and G[row + 1][col] == 'L' and not visited[row + 1][col]:
            parent[row + 1][col] = (row, col)
            q.append((row + 1, col, dist + 1))

        if 0 <= row < n and 0 <= col - 1 < n and G[row][col - 1] == 'L' and not visited[row][col - 1]:
            parent[row][col - 1] = (row, col)
            q.append((row, col - 1, dist + 1))

        if 0 <= row < n and 0 <= col + 1 < n and G[row][col + 1] == 'L' and not visited[row][col + 1]:
            parent[row][col + 1] = (row, col)
            q.append((row, col + 1, dist + 1))

    prev = parent[n - 1][n - 1]
    path = []

    while prev is not None:
        path.append(prev)
        prev = parent[prev[0]][prev[1]]

    path.reverse()

    return path

T = [["L", "W", "L", "L", "L", "L", "L", "L"],
     ["L", "W", "L", "W", "W", "L", "L", "L"],
     ["L", "L", "L", "W", "W", "L", "W", "L"],
     ["L", "W", "W", "W", "W", "L", "W", "L"],
     ["L", "L", "W", "W", "L", "L", "L", "L"],
     ["L", "W", "L", "L", "L", "W", "W", "W"],
     ["W", "W", "L", "W", "L", "L", "W", "L"],
     ["L", "L", "L", "L", "L", "L", "L", "L"]]

print(bfs(T))