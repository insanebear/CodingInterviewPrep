"""
<https://leetcode.com/problems/unique-paths/>
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        count = [1] * n

        for row in range(1, m):
            new_count = [1] * n
            for col in range(1, n):
                new_count[col] = new_count[col - 1] + count[col]

            count = new_count

        return count[-1]
