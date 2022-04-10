def solution(m, n, puddles):
    board = [[ 0 for _ in range(n)] for _ in range(m)]
    
    # puddle adjustment
    for puddle in puddles:
        # index starts 1 -> 0 base
        puddle[0] -= 1
        puddle[1] -= 1

    # calculate the number
    for x in range(m):
        for y in range(n):
            if x == 0 and y == 0:
                board[0][0] = 1
            elif [x, y] in puddles:
                board[x][y] = 0
            else:
                if x-1 >= 0 and y-1 >= 0:
                    board[x][y] = board[x-1][y] + board[x][y-1]
                elif x-1 < 0:
                    board[x][y] = board[x][y-1]
                elif y-1 < 0:
                    board[x][y] = board[x-1][y]
    
    return board[m-1][n-1] % 1000000007