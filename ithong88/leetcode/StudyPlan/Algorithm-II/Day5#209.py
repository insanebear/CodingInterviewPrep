class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        answer = len(nums) + 1
        start, end = 0, 0
        sum = nums[0]
        while start < len(nums) and end < len(nums):
            if sum >= target:
                answer = min(answer, end - start + 1)
                sum -= nums[start]
                if start < end:
                    start += 1
                else:
                    start += 1
                    end += 1
                    if end == len(nums):
                        break
                    sum += nums[end]
            else:
                end += 1
                if end == len(nums):
                    break
                sum += nums[end]
        if answer > len(nums):
            answer = 0
        return answer
