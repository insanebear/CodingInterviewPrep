class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        # dp[i]: s[:i] can be segmented with dictionary words or not
        dp = [False for _ in range(20)]

        for i in range(len(s)):
            start = max(i - 20, 0)
            update = False
            # check post 20 words
            for j in range(start, i + 1):
                check_idx = (j + 19) % 20
                check = j == 0 or dp[check_idx]

                cur = i % 20

                if check and s[j:i + 1] in wordSet:
                    dp[cur] = True
                    update = True
            dp[cur] = update

        # print(dp)
        check_idx = (len(s) + 19) % 20
        # print(check_idx)
        return dp[check_idx]