"""
<https://leetcode.com/problems/search-a-2d-matrix/>
"""


from types import List


class Solution:
    def binary_search(self, nums: list[int], target: int) -> int:
        """
        return index of target, or the largest element among smaller items than target
        """
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if target < nums[mid]:
                right = mid
            else:
                left = mid + 1

        if left == len(nums) or target < nums[left]:
            left -= 1
        return left

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search from the list of [first items of each row]
        # the last row that starts with smaller element than target: the row who might contains target
        # do binary search of target
        row_starts = [row[0] for row in matrix]

        row_index = self.binary_search(row_starts, target)
        print(row_index)
        col_index = self.binary_search(matrix[row_index], target)

        return matrix[row_index][col_index] == target
