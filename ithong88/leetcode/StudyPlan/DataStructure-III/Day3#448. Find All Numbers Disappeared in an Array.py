class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        answer = [i + 1 for i in range(len(nums))]
        # print(answer)
        answer = set(answer)
        for num in nums:
            answer.discard(num)
        answer = list(answer)
        return answer
