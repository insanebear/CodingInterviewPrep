"""
<https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/>
"""

from types import List


class Solution:
    def before_index(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)

        while start < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid
        return start

    def after_index(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)

        while start < end:
            mid = (start + end) // 2
            if nums[mid] <= target:
                start = mid + 1
            else:
                end = mid
        return start

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.before_index(nums, target)
        right = self.after_index(nums, target)

        if right <= left:
            return [-1, -1]
        else:
            return [left, right - 1]
