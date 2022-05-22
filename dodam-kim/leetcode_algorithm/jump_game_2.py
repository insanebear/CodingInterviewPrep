"""
<https://leetcode.com/problems/jump-game-ii/>
"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        jump_count = 0
        curr_jump = 0
        next_jump = 0

        for jump_start in range(len(nums)):
            next_jump = max(next_jump, jump_start + nums[jump_start])

            if jump_start == curr_jump:
                jump_count += 1  # needs 1 more jump to go over current position
                curr_jump = next_jump

        return jump_count
