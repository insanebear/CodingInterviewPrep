"""
<https://leetcode.com/problems/house-robber-ii/>
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_between(start: int, last: int) -> int:
            money_stack = [0, 0]

            for i in range(start, last):
                money = max(money_stack[0] + nums[i], money_stack[1])
                money_stack = [money_stack[1], money]

            return money_stack[1]

        return max(rob_between(0, len(nums) - 1), rob_between(1, len(nums)))
