class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answers = set()
        def dfs(answer, t):
            if t == 0:
                sorted_answer = tuple(sorted(answer))
                answers.add(sorted_answer)
            
            elif min(candidates) <= t:
                for num in candidates:
                    dfs(answer + [num], t-num)
        
        for num in candidates:
            dfs([num], target-num)
        print(answers)
        return list(answers)