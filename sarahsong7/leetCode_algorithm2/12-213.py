class Solution:
    def rob(self, nums: List[int]) -> int:
        dp0 = nums[0:len(nums)-1]
        dp1 = nums[1:len(nums)]
        
        if len(nums) <= 3:
            return max(nums)
        
        dp0[1] = max(dp0[0],dp0[1])
        dp1[1] = max(dp1[0],dp1[1])
        
        for i in range(2,len(dp0)):
            dp0[i]=max(dp0[i-2]+dp0[i], dp0[i-1])
            dp1[i]=max(dp1[i-2]+dp1[i], dp1[i-1])
        
        return max(dp0[len(dp0)-1], dp1[len(dp1)-1])
        