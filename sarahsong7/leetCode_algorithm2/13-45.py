class Solution:
    def jump(self, nums: List[int]) -> int:
        # dp[i]= the minimum number of jump
        if len(nums) == 1:
            return 0
        dp = [len(nums)]*len(nums)
        for col in range(1, min(1+nums[0], len(nums))):
            dp[col] = 1
        
        for row in range(1,len(nums)):
            if dp[len(nums)-1] < len(nums):
                return dp[len(nums)-1]
            for col in range(row+1,min(row+1+nums[row],len(nums))):
                dp[col] = min(dp[row]+1, dp[col])
        return dp[len(nums)-1]
            