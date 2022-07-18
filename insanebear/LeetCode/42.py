class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = []
        
        for i, e in enumerate(height):
            
            # pop items until top is greater than input e
            while stack and e > height[stack[-1]]:
                s_height = stack.pop() # pop the smallest height until now
                
                if stack:
                    top = stack[-1]
                    w = i-top-1 # calculate width using index
                    h = min(e, height[top]) - height[s_height] # calculate height diff
                    ans += (w * h)
            
            # push current height
            stack.append(i)
        return ans