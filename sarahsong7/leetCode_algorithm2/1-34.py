class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(nums)-1
        min_num = -1
        mid = -1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
                
        if len(nums)!= 0 and nums[mid] == target:
            min_num= mid
        elif (len(nums) > mid+1) and (nums[mid+1] == target):
            min_num = mid+1
        
        left = 0
        right = len(nums)-1
        max_num = -1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
            
        
        if len(nums)!=0 and nums[mid] == target:
            max_num = mid
        elif len(nums)!=0 and (nums[mid-1] == target):
            max_num = mid-1
            
        answer = [min_num, max_num]
        
        return answer