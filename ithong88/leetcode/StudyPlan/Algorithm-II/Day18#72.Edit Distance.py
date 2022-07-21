class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[i + j for i in range(len(word1) + 1)] for j in range(len(word2) + 1)]

        for i, c2 in enumerate(word2):
            for j, c1 in enumerate(word1):
                if c1 == c2:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = min(dp[i][j], dp[i][j + 1], dp[i + 1][j]) + 1

        return dp[-1][-1]