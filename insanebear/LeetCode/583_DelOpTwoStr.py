class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
            word1 <> word2 longest subseq length -> l
            (len(word1) - l) + (len(word2) - l)
        """
        
        dp = [[ 0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        m = dp[-1][-1]
        
        return (len(word1) - m) + (len(word2) - m)