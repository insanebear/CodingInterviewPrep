class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for num in nums:
            if len(dp) == 0:
                dp = [num]
            elif num > dp[-1]:
                dp.append(num)
            else:
                prev = -100000
                for j in range(0, len(dp)):
                    if dp[j] > num and num > prev:
                        dp[j] = num
                        break
                    prev = dp[j]

        return len(dp)
