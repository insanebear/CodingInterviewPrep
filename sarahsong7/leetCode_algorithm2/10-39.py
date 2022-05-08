from itertools import product
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        left = []
        same = []
        smallest = target
        for cd in candidates:
            if cd < target:
                left.append(cd)
                if smallest > cd:
                    smallest = cd
            elif cd == target:
                same.append(cd)
                
        if len(same)>0:
            answer.append([target])
        
        dic = dict()
        s_left = []
        for i in range(target//smallest):
            s_left.append(left)
            for item in product(*s_left):
                """
                  l1      l2     l3
                  [[1,2,3][2,3,4][4,5,6]]
                  (1,2,4),(1,3,4).....
                  product(*s_left)=product(l1,l2,l3)
                """
                sorted_item=tuple(sorted(item))

                if sorted_item not in dic:
                    dic[sorted_item] = 0
                    if sum(list(sorted_item)) == target:
                        answer.append(list(sorted_item))
        return answer
        