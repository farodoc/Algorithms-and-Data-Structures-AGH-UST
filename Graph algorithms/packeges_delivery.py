# Byteland is a land containing N cities and N-1 two-way roads. The road system creates a consistent
# graph. We are given a list of K cities to which we have to deliver packages and being able to start
# and finish the route in any city, find the minimum distance that we must travel to deliver all packages.


def packages_delivery(G):
    
















graph = [[1], [0, 2], [1, 3, 4], [2, 6], [2, 5], [4], [3, 7, 8], [6], [6, 9, 10, 11],
         [8], [8], [8, 12, 16], [11, 13, 14], [12, 15], [12], [13], [11, 17, 18], [16], [16]]

k = [1, 5, 7, 10]
print(packages_delivery(graph))