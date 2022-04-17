class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        mid = (l+r) // 2
        
        while l <= r:
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else: # target == nums[mid]
                s, f = mid, mid
                
                while s-1 >= 0 and nums[mid] == nums[s-1]:
                    s -= 1
                while f+1 <= len(nums)-1 and nums[mid] == nums[f+1]:
                        f += 1
                    
                return [s, f]
            mid = (l+r) // 2
        
        return [-1, -1]
"""
Another trial

import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return(-1, -1)
        return(bisect_left(nums, target), bisect_right(nums, target)-1)
"""