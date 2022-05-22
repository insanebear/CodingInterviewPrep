class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_pos = nums[0]
        i = 1
        while i <= max_pos and i < len(nums):
            max_pos = max(max_pos, i + nums[i])
            if max_pos >= len(nums) - 1:
                return True
            i += 1

        return max_pos >= len(nums) - 1