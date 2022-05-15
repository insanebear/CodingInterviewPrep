class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        if length == 1:
            return True
        dp = [False]*length
        for col in range(1, min(1+nums[0], length)):
            dp[col] = True
            
        for row in range(1,length):
            if not dp[row]:
                return False
            if dp[length-1]:
                return True
            for col in range(row+1,min(row+1+nums[row],length)):
                dp[col] = True
                
        if dp[length-1]:
            return True
        else:
            return False
        