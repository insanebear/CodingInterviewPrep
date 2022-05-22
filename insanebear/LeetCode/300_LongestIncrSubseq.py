class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [ 1 for _ in range(len(nums))]
        """
            dp[i] = length of the longest increasing sequence including nums[i]
        """
        for r in range(len(nums)):
            for l in range(r):
                if nums[l] < nums[r]: # increasing seq
                    if dp[l] + 1 > dp[r]:
                        dp[r] = dp[l] + 1
        
        return max(dp)