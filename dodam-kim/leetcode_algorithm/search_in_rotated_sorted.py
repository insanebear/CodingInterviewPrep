"""
<https://leetcode.com/problems/search-in-rotated-sorted-array/>
"""


from types import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums))

    def binary_search(self, nums: List[int], target: int, left: int, right: int) -> int:
        if right <= left:
            return -1

        mid = (left + right) // 2
        if target == nums[mid]:
            return mid

        if target < nums[mid]:
            index = self.binary_search(nums, target, left, mid)
            if nums[right - 1] == target:
                return right - 1
            if index == -1 and target <= nums[right - 1]:
                # in nums[mid:right], there are some numbers gte nums[mid] & some numbers lte nums[right - 1]
                index = self.binary_search(nums, target, mid + 1, right)
            return index
        else:
            index = self.binary_search(nums, target, mid + 1, right)
            if nums[left] == target:
                return left
            if index == -1 and nums[left] <= target:
                index = self.binary_search(nums, target, left, mid)

        return index
