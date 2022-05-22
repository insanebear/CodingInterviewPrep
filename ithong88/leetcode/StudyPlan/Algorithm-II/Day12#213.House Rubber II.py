class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]

        dp = [[0 for _ in range(len(nums))], [0 for _ in range(len(nums))]]
        # print(dp)

        # rub first house
        dp[0][0] = nums[0]
        dp[0][1] = max(nums[0], nums[1])

        # do not rub first house
        dp[1][1] = nums[1]

        for i in range(2, len(nums)):
            dp[0][i] = max(nums[i] + dp[0][i - 2], dp[0][i - 1])
            dp[1][i] = max(nums[i] + dp[1][i - 2], dp[1][i - 1])

        return max(dp[0][-2], dp[1][-1])
