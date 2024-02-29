from egzP9btesty import runtests

def sol( G, R ):
	n = len(G)

	G2 = [[0 for _ in range(n)] for _ in range(n)]

	for u in range(n):
		for v in G[u]:
			G2[u][v] += 1

	for u in range(n):
		for v in R[u]:
			G2[u][v] -= 1
        
	path = []

	def DFS(G, s):
		for i in range(n):
			if G[s][i] >= 1:
				G[s][i] -= 1
				DFS(G, i)

		path.append(s)

	DFS(G2, 0)
	path.reverse()

	return path
	
runtests(sol, all_tests=True)