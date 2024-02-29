def nwd(a, b):
    while b != 0:
        a, b = b, a % b

    return a 

def race(T):
    movesLeft = 10**10
    movesRight = 10**10

    def left_rook(row, col, moves):
        nonlocal movesLeft
        n = len(T)

        if row == n - 1 and col == n - 1:
            movesLeft = min(movesLeft, moves)
            return

        ruch = 1

        while ruch + col < n:
            if nwd(T[row][col], T[row][ruch + col]) == 1:
                left_rook(row, col + ruch, moves + 1)

            ruch += 1
        
        ruch = 1
        
        while ruch + row < n:
            if nwd(T[row][col], T[row + ruch][col]) == 1:
                left_rook(row + ruch, col, moves + 1)

            ruch += 1

    def right_rook(row, col, moves):
        nonlocal movesRight
        n = len(T)

        if row == n - 1 and col == 0:
            movesRight = min(movesRight, moves)
            return

        ruch = 1

        while col - ruch >= 0:
            if nwd(T[row][col], T[row][col - ruch]) == 1:
                right_rook(row, col - ruch, moves + 1)

            ruch += 1
        
        ruch = 1
        
        while ruch + row < n:
            if nwd(T[row][col], T[row + ruch][col]) == 1:
                right_rook(row + ruch, col, moves + 1)

            ruch += 1
    
        right_rook(0, len(T) - 1, 0)
        left_rook(0, 0, 0)

        if movesLeft == movesRight:
            return 0

        if movesRight == 0:
            return 1

        if movesLeft == 0:
            return 2

        if movesLeft > movesRight:
            return 2

        if movesLeft < movesRight:
            return 1