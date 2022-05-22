"""
<https://leetcode.com/problems/backspace-string-compare/>
"""
from typing import List

# Stack
class Solution:
    def typing(self, s: str) -> list[str]:
        output_s = []
        for c in s:
            if c != "#":
                output_s.append(c)
            elif output_s:
                output_s.pop()
        return output_s

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.typing(s) == self.typing(t)


# Reversed string
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def type_result(string) -> List[str]:
            typed_chars = []
            skip = 0
            for c in string:
                if c == "#":
                    skip += 1
                elif skip > 0:
                    skip -= 1
                else:
                    typed_chars.append(c)

            return typed_chars

        typing_s = type_result(reversed(s))
        typing_t = type_result(reversed(t))

        return typing_s == typing_t


# yield
class Solution:
    def next_index(self, typings: str) -> int:
        skip = 0
        for c in reversed(typings):
            if c == "#":
                skip += 1
            elif skip > 0:
                skip -= 1
            else:
                yield c
        yield ""

    def backspaceCompare(self, s: str, t: str) -> bool:
        for s_next, t_next in zip(self.next_index(s), self.next_index(t)):
            if s_next != t_next:
                return False

        return True
