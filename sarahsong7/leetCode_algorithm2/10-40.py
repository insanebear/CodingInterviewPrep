class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        dic = set()
        check = [i*(-1) for i in candidates]
        for i in range(len(candidates)):
            recur(candidates, dic, answer, [], i, target, check)
        
        return answer
    
def recur(candidates, dic, answer, new_list, pos, target, check):
    if check[pos]>0:
        return
    new_check=check.copy()
    new_check[pos] = -check[pos]
    copy = list(new_list)
    copy.append(candidates[pos])
    if tuple(sorted(copy)) in dic:
        return
    total = sum(copy)

    dic.add(tuple(sorted(copy)))
    if total > target:
        return
    elif total == target:
        answer.append(copy)
    else:
        for i in range(len(candidates)):
            recur(candidates, dic, answer, copy, i, target, new_check)