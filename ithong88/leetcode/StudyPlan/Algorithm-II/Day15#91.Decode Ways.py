class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        if len(s) < 2:
            return 1

        # initialize
        dp = [0 for _ in range(len(s))]
        # dp[n] = dp[n-2] + dp[n-1]
        # dp[n-2] : decode (0 ~ n-2) and add (n-1 ~ n)
        # if (n-1 ~ n) is a character

        # dp[n-1] : decode (0 ~ n-1) and add (n)
        # if n is a character

        # initial condition
        dp[0] = 1
        encode = int(s[0:2])
        check_single = int(s[1]) != 0
        check_double = encode <= 26
        if check_single:
            dp[1] += dp[0]
        if check_double:
            dp[1] += 1

        for i in range(2, len(s)):
            encode = int(s[i - 1:i + 1])
            check_single = int(s[i]) != 0
            check_double = int(s[i - 1]) != 0 and encode <= 26
            if check_single:
                dp[i] += dp[i - 1]
            if check_double:
                dp[i] += dp[i - 2]

            if dp[i - 1] == 0 and dp[i - 2] == 0:
                return 0
        # print(dp)
        return dp[-1]