class Solution:
    def findMin(self, nums: List[int]) -> int:
        idx = -1
        rotate, left, right = 0, 0, len(nums) - 1

        if len(nums) > 1:
            while left <= right:
                mid = (left + right) // 2
                # print(f'left:{left}, right:{right}, mid:{mid}, nums[mid]:{nums[mid]}')
                if mid == len(nums) - 1:
                    rotate = 0
                    break

                if nums[mid] > nums[mid + 1]:
                    rotate = mid + 1
                    break

                if left == right:
                    rotate = 0
                    break

                if nums[left] < nums[mid]:
                    left = mid + 1
                else:
                    right = mid

        return nums[rotate]