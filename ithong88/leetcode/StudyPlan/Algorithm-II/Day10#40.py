class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def find(comb, num, cur_idx, answer):
            if num == 0:
                answer.append(list(comb))
                return
            elif num < 0:
                return

            for next_idx in range(cur_idx, len(candidates)):
                if next_idx > cur_idx and candidates[next_idx] == candidates[next_idx - 1]:
                    continue

                # print(cur_idx, candidates[cur_idx], next_idx, candidates[next_idx], comb)
                candidate = candidates[next_idx]

                comb.append(candidate)
                find(comb, num - candidate, next_idx + 1, answer)
                comb.pop()

        answer = []
        candidates.sort()
        find([], target, 0, answer)

        return answer