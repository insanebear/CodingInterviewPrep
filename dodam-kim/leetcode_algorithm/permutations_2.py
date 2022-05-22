"""
<https://leetcode.com/problems/permutations-ii/>
"""

from typing import List


class Solution:
    def extend_permutation(
        self,
        nums: List[int],
        used: List[int],
        current: List[int],
        permutations: List[List[int]],
    ):
        if len(current) == len(nums):
            permutations.append(current.copy())
            return

        for i, n in enumerate(nums):
            if used[i]:
                continue
            if i > 0 and n == nums[i - 1] and used[i - 1] is False:
                continue
            used[i] = True
            current.append(n)
            self.extend_permutation(nums, used, current, permutations)
            used[i] = False
            current.pop()

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        used = [False] * len(nums)
        permutations = []
        self.extend_permutation(nums, used, [], permutations)

        return permutations
