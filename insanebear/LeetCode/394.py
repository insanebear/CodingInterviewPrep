class Solution:
    def decodeString(self, s: str) -> str:
        string = [c for c in s]
        stack = []
        temp = ""
        
        while len(string) != 0:
            c = string.pop()
            
            if c == "[":
                # pop from stack until seeing "]"
                e = stack.pop()
                while e != "]":
                    temp += e
                    e = stack.pop()
                stack.append(temp)
                temp = ""
            elif c.isdigit():
                number = c
                while number:
                    temp = number + temp
                    if len(string) != 0 and string[-1].isdigit():
                        number = string.pop()
                    else:
                        number = None
                
                e = stack.pop()
                stack.append(e*int(temp))
                temp = ""             
                
            else:
                # put everthing in a stack
                stack.append(c)
        
        ans = ""
        while stack:
            ans += stack.pop()
        
        return ans