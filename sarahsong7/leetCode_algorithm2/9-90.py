from itertools import combinations

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        dic = set()
        answer = [[]]
    
        for i in range(1,len(nums)+1):
            for item in combinations(nums,i):
                sorted_item=tuple(sorted(item))

                if sorted_item not in dic:
                    dic.add(sorted_item)
                    answer.append(list(sorted_item))
        
        return answer