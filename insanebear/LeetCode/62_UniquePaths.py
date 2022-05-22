class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        board = [ [ 1 for _ in range(n) ] for _ in range(m) ]
        
        for i in range(1, m):
            for j in range(1, n):
                board[i][j] = board[i-1][j] + board[i][j-1]
        
        return board[m-1][n-1]