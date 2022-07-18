class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        ans = []
        
        for n in num:
            while k!=0 and ans and n < ans[-1]:
                ans.pop()
                k -= 1
                
            if ans or n != "0": # except only the leading 0
                ans.append(n)
            
        if k != 0: # if k left
            ans = ans[:-k]
            
        return "".join(ans) or "0"
