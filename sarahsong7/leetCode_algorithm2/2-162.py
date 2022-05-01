class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left=0
        right = len(nums)-1
        mid = 0
        if left == right:
            return left
        # print()
        while left<right:
            
            mid = (left+right)//2
            # print(left,mid,right)
            if nums[mid] > nums[left]:
                if mid>0 and nums[mid-1]<nums[mid]:
                    left = mid
                elif mid>0 and nums[mid-1]>nums[mid]:
                    right = mid
            elif nums[mid] == nums[left]:
                if mid<len(nums)-1 and nums[mid]<nums[mid+1]:
                    left = mid+1
                    mid = mid+1
                elif mid<len(nums)-1 and nums[mid]>nums[mid+1]:
                    right = mid
                else:
                    right = mid
            else:
                right = mid
        return mid