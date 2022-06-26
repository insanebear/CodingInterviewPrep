class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        nums.sort() # n log n

        maxlen = 1
        l = 1
        
        for i in range(1, len(nums)):
            if nums[i-1] + 1 == nums[i]:
                l += 1
            elif nums[i-1] == nums[i]:
                pass
            else:
                if maxlen < l:
                    maxlen = l
                l = 1
        
        if maxlen < l:
            maxlen = l
        
        return maxlen