class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [100000 for _ in range(len(nums))]
        dp[0] = 0
        max_pos = 0
        for i, jump in enumerate(nums):
            distance = min(i + jump, len(nums))
            if distance > max_pos:
                if distance >= len(nums) - 1:
                    return min(dp[i] + 1, dp[-1])

                for j in range(max_pos, distance + 1):
                    dp[j] = min(dp[i] + 1, dp[j])

                max_pos = distance

        return dp[-1]