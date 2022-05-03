class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right = len(nums)-1
        mid = 0
        if left == right:
            return nums[left]
        while left<right:
            
            mid = (left+right)//2
            print(left,mid,right)
            if nums[mid] < nums[left] and nums[right]>nums[mid]:
                right = mid
            elif nums[mid] < nums[left] and nums[right]<nums[mid]:
                left = mid
            elif nums[mid] > nums[left] and nums[right]<nums[mid]:
                left = mid
            elif nums[mid] > nums[left] and nums[right]>nums[mid]:
                right = mid
            elif nums[mid] == nums[left]:
                if mid<len(nums)-1 and nums[mid]>nums[mid+1]:
                    return nums[mid+1]
                elif mid<len(nums)-1 and nums[mid]<nums[mid+1]:
                    return nums[mid]
                else:
                    return nums[mid]
                
            