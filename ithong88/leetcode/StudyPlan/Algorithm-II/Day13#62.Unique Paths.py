class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        dp[1][1] = 1

        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if row == 1 and col == 1: continue
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        return dp[m][n]