class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        m = (l+r) // 2
        
        while m > 0 and m < len(nums)-1 :
            if nums[m] < nums[m-1]:
                r = m - 1
            elif nums[m] < nums[m+1]:
                l = m + 1
            else:
                return m
            
            m = (l+r) // 2
        if m == 0:
            peak = max(nums[m],nums[r])
            return nums.index(peak)
        return m