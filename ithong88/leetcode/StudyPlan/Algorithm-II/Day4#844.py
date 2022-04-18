class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        new_s = new_t = ''

        for i in s:
            if i != '#':
                new_s += i
            else:
                new_s = new_s[:-1]

        for j in t:
            if j != '#':
                new_t += j
            else:
                new_t = new_t[:-1]

        return new_s == new_t
