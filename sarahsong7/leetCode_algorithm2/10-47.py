from itertools import permutations

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        answer = []
        dic = set()
        for item in permutations(nums,len(nums)):
            if item not in dic:
                dic.add(item)
                answer.append(list(item))
        
        return answer