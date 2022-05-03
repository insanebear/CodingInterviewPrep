from itertools import combinations
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        if len(nums)<3:
            return []
        dic = dict()
        for i,num in enumerate(nums):
            if num in dic:
                dic[num] = dic[num]+1
            else:
                dic[num] = 0
        coms = list(combinations(nums,2))
        for com in coms:
            if -(com[0]+com[1]) in dic:
                if com[0] == -(com[0]+com[1]) and com[1] == -(com[0]+com[1]) and com[0]==com[1]:
                    if dic[-(com[0]+com[1])]<3:
                        continue
                elif com[0] == -(com[0]+com[1]) or com[1] == -(com[0]+com[1]):
                    if dic[-(com[0]+com[1])]<2:
                        continue
                
                c = tuple(sorted([com[0],com[1],-(com[0]+com[1])]))
                answer.add(c)
        return answer

        
        