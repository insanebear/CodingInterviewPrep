class Solution:
    def shortestPalindrome(self, s: str) -> str:

        def recShortestPalindrome(s):
            n = len(s)
            i = 0
            for j in range(n - 1, -1, -1):
                if s[i] == s[j]:
                    i += 1

            if i == n:
                return s
            rev = s[i:n]
            rev = rev[::-1]
            return rev + recShortestPalindrome(s[0:i]) + s[i:]

        return recShortestPalindrome(s)
