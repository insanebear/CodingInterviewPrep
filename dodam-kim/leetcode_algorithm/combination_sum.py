"""
<https://leetcode.com/problems/combination-sum/>
"""
from typing import List

# Backtracking Approach
class Solution:
    def extend_combination(
        self, current: List[int], index: int, target: int, combinations: List[List[int]]
    ):
        if target == 0:
            combinations.append(current)

        for i in range(index, len(self.candidates)):
            cand = self.candidates[i]
            if cand <= target:
                self.extend_combination(
                    current + [cand], i, target - cand, combinations
                )

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        [2, 3, 6, 7]
        ->
        [7, 6, 3, 2]
        target: int
        index: int
        current: List[int]
        combinations: List[List[int]]
        """
        self.candidates = candidates
        combinations = []
        self.extend_combination([], 0, target, combinations)

        return combinations


# Memoization
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # candidates.sort(reverse=True)

        dp = [[] for _ in range(target + 1)]
        dp[0].append([])

        """
        dp[target] = dp[target - n] for n in candidates
        """
        for n in candidates:
            for prev_sum in range(len(dp)):
                if prev_sum + n >= len(dp):
                    continue
                if not dp[prev_sum]:
                    continue
                for base in dp[prev_sum]:
                    dp[prev_sum + n].append(base + [n])

        return dp[target]
