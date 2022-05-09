class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def find(comb, num, answer):
            if num == 0:
                comb.sort()
                if comb not in answer:
                    answer.append(comb)
                return
            elif num < 0:
                return
            else:
                for candidate in candidates:
                    find(comb + [candidate], num - candidate, answer)

        answer = []
        find([], target, answer)
        return answer

