class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums)<3:
            return 0
        
        answer = 0
        dp = [-2001 for _ in range(len(nums))] 
        
        for first in range(0,len(nums)-2):
            if nums[first+1]-nums[first] == nums[first+2]-nums[first+1]:
                dp[first]=nums[first+1]-nums[first]
                answer=answer+1
        for first in range(0,len(nums)-2):
            for size in range(3,len(nums)-first):
                if dp[first] == nums[first+size]-nums[first+size-1]:
                    answer= answer+1
                else:
                    break
        return answer