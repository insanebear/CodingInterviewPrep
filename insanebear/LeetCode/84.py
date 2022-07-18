class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
            while stack top >= current h value:
                pop an element from stack and calculate area
                update max area
            
            push current h value to stack
        """
        
        stack = [] # contains index in increasing order -> contains kind of barriers
        heights.append(0) # to calculate width at final round
        area = 0
        
        for i, height in enumerate(heights):
            
            # stack has elements and top is greater than current height
            while stack and heights[stack[-1]] > height:
                h = heights[stack.pop()]
                w = i - stack[-1] -1 if stack else i # if there's no elem, h is the smallest height and no barrier until i -> width should be i
                
                area = max(area, w*h)
            
            stack.append(i)
        
        return area
                