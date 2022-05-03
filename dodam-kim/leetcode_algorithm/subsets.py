"""
<https://leetcode.com/problems/subsets/>
"""

from typing import List

# Iterative approach
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset_list = [[]]

        for n in nums:
            new_subset = []
            for s in subset_list:
                new_subset.append(s + [n])
            subset_list.extend(new_subset)

        return subset_list
