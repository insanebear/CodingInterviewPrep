from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits is "":
            return []
        letters = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        
        items = []
        for num in digits:
            items.append(letters[int(num)])
        
        temp = product(*items)
        answer = []
        
        for item in temp:
            answer.append(''.join(item))
        return answer
