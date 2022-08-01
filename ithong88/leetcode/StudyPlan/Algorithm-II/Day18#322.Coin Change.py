class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [10001 for _ in range(amount + 1)]
        dp[0] = 0
        cur = 0
        min_coin = min(coins)
        while cur < amount:
            if dp[cur] == 10001:
                cur += 1
                continue
            for coin in coins:
                next_pos = cur + coin
                if next_pos <= amount:
                    dp[next_pos] = min(dp[cur] + 1, dp[next_pos])
            cur += 1

        return -1 if dp[amount] == 10001 else dp[amount]