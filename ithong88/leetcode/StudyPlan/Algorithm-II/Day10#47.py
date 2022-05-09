class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def permutation(cur, remains, answer):
            if len(remains) == 0 and cur not in answer:
                answer.append(cur)
                return

            for i, num in enumerate(remains):
                new_remains = remains.copy()
                new_remains.pop(i)
                permutation(cur + [num], new_remains, answer)

        permutation([], nums, answer)
        return answer

