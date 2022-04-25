class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def stack_operation(string):
            stack = []
            for c in string:
                if c == '#':
                    if len(stack) != 0: 
                        stack.pop()
                else:
                    stack.append(c)
        
            return stack
        
        s = stack_operation(s)
        t = stack_operation(t)
        
        return True if s == t else False