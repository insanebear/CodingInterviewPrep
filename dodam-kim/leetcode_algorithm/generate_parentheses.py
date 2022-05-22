"""
<https://leetcode.com/problems/generate-parentheses/>
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parenthesis = []

        def extend(curr: List[str], left, right):
            if left == n and right == n:
                parenthesis.append("".join(curr))
                return

            if left < n:
                curr.append("(")
                extend(curr, left + 1, right)
                curr.pop()

            if left > right:
                curr.append(")")
                extend(curr, left, right + 1)
                curr.pop()

        extend([], 0, 0)
        return parenthesis
