class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        board = [[False] * n  for _ in range(n)]
        ans = ""
        
        for i in range(n):
            # Palindrome length 1
            board[i][i] = True
            ans = s[i]
        
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j] and (i+1 == j or board[i+1][j-1]):
                        board[i][j] = True
                        
                        if len(s[i:j+1]) > len(ans):
                            ans = s[i:j+1]

        
        return ans