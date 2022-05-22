class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [ 1 for _ in range(len(nums))]
        dp_cnt = [ 1 for _ in range(len(nums))]

        for r in range(len(nums)):
            for l in range(r):
                if nums[l] < nums[r]:
                    if dp[l] + 1 > dp[r]:
                        dp[r] = dp[l] + 1 # update using index l value
                        dp_cnt[r] = dp_cnt[l]
                    elif dp[l] + 1 == dp[r]:
                        dp[r] = dp[l] + 1
                        dp_cnt[r] += dp_cnt[l]
        
        """     012345678
                111222333
          dp    111222333
          dpcnt 111333999
        
        """
        
        m = max(dp)
        indicies = set()
        for i, n in enumerate(dp):
            if n == m:
                indicies.add(i)
        
        ans = 0
        for i in indicies:
            ans += dp_cnt[i]
        
        return ans