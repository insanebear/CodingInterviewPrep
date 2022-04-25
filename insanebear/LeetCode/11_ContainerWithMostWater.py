class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        max_area = 0
        while i < j:
            max_area = max(max_area, (j-i) * min(height[i], height[j]))
            
            if height[i] <= height[j] and height[i+1] >= height[j]:
                i += 1
            elif height[j] <= height[i] and height[j-1] >= height[i]:
                j -= 1
            else:
                if height[i] < height[j]:
                    i += 1
                else:
                    j -= 1
        
        return max_area