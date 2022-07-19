class Solution:
    def shortestPalindrome(self, s):
        r, n = s[::-1], len(s)
        for i in range(n):
            f, b = s[:n - i], r[i:]
            if f == b: return r[:i] + s
        return ""