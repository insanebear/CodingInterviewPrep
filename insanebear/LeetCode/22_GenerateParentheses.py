class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answers = []
        def dfs(comb, left, right):
            if left == 0:
                for _ in range(right):
                    comb += ")"
                answers.append(comb)
            elif left < right:
                dfs(comb+"(", left-1, right)
                dfs(comb+")", left, right-1)
            else:
                dfs(comb+"(", left-1, right)
        
        dfs("", n, n)
        return answers