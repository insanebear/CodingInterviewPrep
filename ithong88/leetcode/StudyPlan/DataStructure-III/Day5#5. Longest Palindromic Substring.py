class Solution:
    def longestPalindrome(self, s: str) -> str:
        # length of longest palindrome start at index i
        # dp[i][j] = string that starts with index i and length j is palindrome or not
        dp = [[False for _ in range(len(s) + 1)] for _ in range(len(s) + 1)]
        answer = s[0]
        max_len = 1
        # print(s[0:1])
        for i in range(len(s) + 1):
            dp[i][0] = dp[i][1] = True

        for length in range(2, len(s) + 1):
            for start in range(len(s) - length + 1):
                last = start + length - 1
                # print(start, last, length, s[start], s[last], dp[start+1][length-2])
                if s[start] == s[last] and dp[start + 1][length - 2]:
                    dp[start][length] = True
                    max_len = length
                    # answer = s[start:start+length]
                    # print(start, length, answer)

        for start in range(len(s)):
            if dp[start][max_len]:
                return s[start:start + max_len]

        return answer

