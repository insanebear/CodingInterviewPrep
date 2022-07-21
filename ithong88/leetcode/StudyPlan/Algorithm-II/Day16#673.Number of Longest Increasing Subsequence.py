class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]  # dp[i]: length of lis
        ways = [1 for _ in range(len(nums))]
        lis = 0
        answer = 0
        for i in range(len(nums)):
            for j in range(i):

                if nums[i] > nums[j] and dp[i] < (dp[j] + 1):
                    dp[i] = dp[j] + 1
                    ways[i] = ways[j]
                elif nums[i] > nums[j] and dp[i] == (dp[j] + 1):
                    ways[i] += ways[j]
            lis = max(lis, dp[i])

        for i in range(len(nums)):
            if dp[i] == lis:
                answer += ways[i]

        return answer
