class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        mid = 0
        while left < right:
            mid = (left+right)//2
            # print(left, mid, right)
            
            if nums[left] == target:
                mid = left
                break
            if nums[right] == target:
                mid = right
                break
            if nums[mid] == target:
                break
            
            if (nums[mid]>=nums[left]) and (nums[left]<target) and (nums[mid]<target) and (nums[right]<target):
                left = mid+1
                right = right-1
            elif (nums[mid]<nums[left]) and (nums[left]<target) and (nums[mid]<target) and (nums[right]<target):
                left = left+1
                right = mid-1
            elif (nums[left]<target) and (nums[mid]<target) and (nums[right]>target):
                left = mid+1
            elif (nums[left]<target) and (nums[mid]>target) and (nums[right]<target):
                right = mid-1
            elif (nums[left]<target) and (nums[mid]>target) and (nums[right]>target):
                right = mid-1
            elif (nums[left]>target) and (nums[mid]<target) and (nums[right]<target):
                left = mid+1
            elif (nums[left]>target) and (nums[mid]<target) and (nums[right]>target):
                left = mid+1
            elif (nums[left]>target) and (nums[mid]>target) and (nums[right]<target):
                left = mid+1
            elif (nums[mid]>=nums[left]) and (nums[left]>target) and (nums[mid]>target) and (nums[right]>target):
                left = mid+1
            elif (nums[mid]<nums[left]) and (nums[left]>target) and (nums[mid]>target) and (nums[right]>target):
                right = mid-1
        
        # print()
        if nums[mid] == target:
            return mid
        if (mid>0) and (nums[mid-1] == target):
            return mid-1
        if (mid<len(nums)-1) and (nums[mid+1] == target):
            return mid+1
        
        return -1