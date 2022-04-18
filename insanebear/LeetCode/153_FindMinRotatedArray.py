class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        m = (l + r) // 2
        
        while r - l != 1:
            if nums[m] > nums[r]:
                l = m
            elif nums[l] > nums[m]:
                r = m
            
            m = (l + r) // 2
            
        return min(nums[l], nums[r])