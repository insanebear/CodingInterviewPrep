class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def combination(nums, idx, answer, cur):
            if idx == len(nums):
                return
            for i in range(idx + 1, len(nums)):
                new_cur = cur.copy()
                new_cur.append(nums[i])
                answer.append(new_cur)
                combination(nums, i, answer, new_cur)

            return answer

        answer = [[]]
        for i, num in enumerate(nums):
            answer.append([num])
            combination(nums, i, answer, [num])

        return answer
