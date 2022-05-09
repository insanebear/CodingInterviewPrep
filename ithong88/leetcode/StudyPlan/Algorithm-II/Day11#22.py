class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []

        def backtrack(comb, left, right, answer):
            # print(comb, left, right, answer)
            if left == right == n:
                answer.append(comb)
                return

            if right > left or left > n or right > n:
                return

            if left > right:
                if left < n:
                    backtrack(comb + '(', left + 1, right, answer)
                backtrack(comb + ')', left, right + 1, answer)

            elif left == right:
                if left < n:
                    backtrack(comb + '(', left + 1, right, answer)

        backtrack('', 0, 0, answer)
        return answer
