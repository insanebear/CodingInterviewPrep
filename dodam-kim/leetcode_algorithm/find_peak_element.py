"""
<https://leetcode.com/problems/find-peak-element/>
"""

from types import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        if right == left:
            return left

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left
