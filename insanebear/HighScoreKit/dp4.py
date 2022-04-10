def solution(money):
    houses = len(money)
    board = [ 0 for _ in range(houses)]
    board2 = [ 0 for _ in range(houses)]
    
    for i in range(houses-1):
        board[i] = max(board[i-1], board[i-2] + money[i])
            
    for i in range(1, houses):
        board2[i] = max(board2[i-1], board2[i-2] + money[i])
        
    return max(max(board), max(board2))