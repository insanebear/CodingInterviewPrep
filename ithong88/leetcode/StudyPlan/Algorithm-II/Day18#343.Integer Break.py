class Solution:
    def integerBreak(self, n: int) -> int:
        # dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        dp = [0 for _ in range(n + 1)]
        dp[2] = 1

        answer = 1

        for i in range(3, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], dp[i - j] * j, (i - j) * j)
                answer = max(answer, dp[i])

        return answer