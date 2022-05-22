"""
<https://leetcode.com/problems/letter-combinations-of-a-phone-number/>
"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def digit_to_string(curr: List[str], index: int):
            if index == len(digits):
                strs.append("".join(curr))
                return

            d = digits[index]
            for c in digit_map[d]:
                curr.append(c)
                digit_to_string(curr, index + 1)
                curr.pop()

        strs = []
        digit_to_string([], 0)
        return strs
