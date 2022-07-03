class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        # to indicate lengths including empty string
        sn = len(s) + 1
        pn = len(p) + 1
        
        # dp board
        dp = [[False] * (pn) for _ in range(sn)] # i = s, j = p
        
        dp[0][0] = True # empty <> empty: always True
        
        # handling * located right after empty string (* includes empty string)
        for j in range(1, pn):
            if p[j-1] != '*':
                break
            dp[0][j] = True
        
        # fill the rest of the board
        for i in range(1, sn):
            for j in range(1, pn):
                if p[j-1] in {'?', s[i-1]}:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
        
        
        return dp[-1][-1]