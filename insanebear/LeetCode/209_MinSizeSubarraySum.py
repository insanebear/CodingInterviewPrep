class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = len(nums)+1
        
        window = 0
        l = 0
        
        for r in range(len(nums)):
            window += nums[r]
            
            while window >= target:
                min_length = min(min_length, r-l+1)
                window -= nums[l]
                l += 1
        
        return 0 if min_length > len(nums) else min_length