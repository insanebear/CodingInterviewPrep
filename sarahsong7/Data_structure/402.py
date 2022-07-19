class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        if len(num) == k:
            return "0"
        
        for val in num:
            while stack and stack[-1] > val and k > 0:
                stack.pop()
                k -= 1
                
            stack.append(val)
        
        for i in range(k):
            stack.pop()
        
        if len(stack) == 0:
            return "0"
        
        return str(int("".join(stack)))