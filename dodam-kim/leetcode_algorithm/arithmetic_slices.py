"""
<https://leetcode.com/problems/arithmetic-slices/>
"""

from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        counts = [0] * len(nums)

        for i in range(2, len(nums)):
            if nums[i - 1] - nums[i - 2] == nums[i] - nums[i - 1]:
                counts[i] = counts[i - 1] + 1

        return sum(counts)
