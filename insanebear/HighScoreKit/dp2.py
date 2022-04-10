import copy
def solution(triangle):
    board = copy.deepcopy(triangle)
    
    for x, elements in enumerate(triangle):
        if x == len(triangle)-1:
            break
        for y in range(len(elements)):
            current = (x, y)
            
            if board[x][y] + triangle[x+1][y] > board[x+1][y]:
                board[x+1][y] = board[x][y] + triangle[x+1][y]
                
            if board[x][y] + triangle[x+1][y+1] > board[x+1][y+1]:
                board[x+1][y+1] = board[x][y] + triangle[x+1][y+1]
            
    return max(board[len(triangle)-1])