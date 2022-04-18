import bisect


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        minus_idx = bisect_left(nums, 0)
        plus_idx = bisect_right(nums, 0)

        minus_nums = nums[:minus_idx]
        plus_nums = nums[plus_idx:]

        if plus_idx - minus_idx >= 3:
            answer.append([0, 0, 0])

        if minus_nums == [] or plus_nums == []:
            return answer

        # Find (minus, 0, plus)
        if minus_idx != plus_idx:
            for minus in minus_nums:
                plus = -1 * minus
                k = bisect_left(plus_nums, plus)
                if k < len(plus_nums) and plus_nums[k] == plus:
                    if [minus, 0, plus] not in answer:
                        answer.append([minus, 0, plus])

        # Find (minus1, minus2, plus)
        for i in range(len(minus_nums)):
            for j in range(i + 1, len(minus_nums)):
                plus = (minus_nums[i] + minus_nums[j]) * -1
                k = bisect_left(plus_nums, plus)
                if k < len(plus_nums) and plus_nums[k] == plus:
                    if [minus_nums[i], minus_nums[j], plus_nums[k]] not in answer:
                        answer.append([minus_nums[i], minus_nums[j], plus_nums[k]])

        # Find (minus, plus1, plus2)
        for j in range(len(plus_nums)):
            for k in range(j + 1, len(plus_nums)):
                # print(plus_nums[j], plus_nums[k])
                minus = (plus_nums[j] + plus_nums[k]) * -1
                i = bisect_left(minus_nums, minus)
                if i < len(minus_nums) and minus_nums[i] == minus:
                    if [minus_nums[i], plus_nums[j], plus_nums[k]] not in answer:
                        answer.append([minus_nums[i], plus_nums[j], plus_nums[k]])

        return answer
