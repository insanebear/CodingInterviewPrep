"""
<https://leetcode.com/problems/combination-sum-ii/>
"""

from typing import List
import collections

# Use collections.Counter
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        counter = collections.Counter(candidates)
        keys = list(counter.keys())

        def extend(
            index: int, curr: List[int], remain: int, combinations: List[List[int]]
        ):
            if remain == 0:
                combinations.append(curr.copy())
                return
            if len(keys) <= index or remain < 0:
                return

            c = keys[index]
            count = counter[c]

            extend(index + 1, curr, remain, combinations)
            for _ in range(count):
                curr.append(c)
                remain -= c
                extend(index + 1, curr, remain, combinations)

            for _ in range(count):
                curr.pop()
                remain += c

        combinations = []
        extend(0, [], target, combinations)

        return combinations


# sort -> skip repeated nums
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def extend(
            index: int, curr: List[int], remain: int, combinations: List[List[int]]
        ):
            if remain == 0:
                combinations.append(curr.copy())
                return
            if remain < 0:
                return

            for next_index in range(index, len(candidates)):
                if (
                    next_index > index
                    and candidates[next_index] == candidates[next_index - 1]
                ):
                    continue

                item = candidates[next_index]
                curr.append(item)
                extend(next_index + 1, curr, remain - item, combinations)
                curr.pop()

        combinations = []
        extend(0, [], target, combinations)

        return combinations
