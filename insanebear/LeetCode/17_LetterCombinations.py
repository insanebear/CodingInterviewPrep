class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combinations = []
        
        phone_dict = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        
        def dfs(comb, depth):
            if depth == len(digits):
                combinations.append("".join(comb))
            else:
                digit = digits[depth]

                for c in phone_dict[digit]:
                    dfs(comb + [c], depth+1)
        if len(digits) != 0:
            dfs([], 0)
        
        return combinations