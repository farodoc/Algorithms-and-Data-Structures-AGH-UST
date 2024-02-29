from egz2btesty import runtests

def magic( C ):
    n = len(C)
    profit = [-1] * n
    profit[0] = 0

    for i in range(n - 1):
        if profit[i] == -1:
            continue

        for j in range(1, 4):
            target, cost = C[i][j][1], C[i][j][0]
            if target == -1:
                continue

            chest_gold = C[i][0]
            curr_gold = profit[i]

            if chest_gold >= cost:
                chest_gold -= cost
                
                if chest_gold > 10:
                    continue

                curr_gold += chest_gold
                profit[target] = max(profit[target], curr_gold)

            else:
                ile_brakuje = cost - chest_gold
                curr_gold -= ile_brakuje

                if curr_gold >= 0:
                    profit[target] = max(profit[target], curr_gold)

    return profit[n - 1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True )

"""C = [ [8, [ 6, 3], [ 4, 2], [7, 1]], # 0
[22, [12, 2], [21, 3], [0,-1]], # 1
[9, [11, 3], [ 0,-1], [7,-1]], # 2
[15, [ 0,-1], [ 1,-1], [0,-1]] ] # 3

print(magic(C))"""

"""C=[[2, [5, 1], [1, 6], [1, 8]],
[2, [7, 2], [1, 4], [1, 2]],
[89, [91, 3], [75, 8], [84, 6]],
[8, [6, 4], [10, 6], [7, 5]],
[4, [5, 5], [1, 7], [3, 5]],
[10, [11, 6], [0, 6], [4, 6]],
[1, [0, 7], [0, 7], [6, 7]],
[57, [51, 8], [45, 8], [50, 8]],
[2, [6, 9], [7, 9], [0, 9]],
[6, [3, -1], [8, -1], [1, -1]]]

print(magic(C))"""