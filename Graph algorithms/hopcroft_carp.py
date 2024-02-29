def hopcroft(T):
    n = len(T)
    unmatched = []
    selected = [-1 for _ in range(n)]

    for source in range(n):
        notFound = True
        for target in T[source]:
            if selected[target] == -1:
                selected[target] = source
                notFound = False
                break

        if notFound:
            unmatched.append(source)

    
    def DFS(source):
        for target in T[source]:
            if not visited[target]:
                visited[target] = True

                if selected[target] == -1 or DFS(selected[target]):
                    selected[target] = source
                    return True
            
        return False
    
    for source in unmatched:
        visited = [False] * n
        DFS(source)

    
    cnt = 0

    for i in range(n):
        if selected[i] != -1:
            cnt += 1

    return cnt