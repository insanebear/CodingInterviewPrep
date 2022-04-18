from bisect import bisect_left, bisect_right

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        left = bisect_left(nums, target)
        if left >= len(nums) or nums[left] != target:
            return [-1, -1]

        right = bisect_right(nums, target)
        right -= 1

        return [left, right]
