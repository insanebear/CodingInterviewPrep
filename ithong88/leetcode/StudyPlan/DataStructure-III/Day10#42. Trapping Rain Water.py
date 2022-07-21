class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        answer = 0
        l_max = r_max = 0

        while l < r:
            if height[l] < height[r]:
                if height[l] >= l_max:
                    l_max = height[l]
                else:
                    answer += l_max - height[l]
                l += 1
            else:
                if height[r] >= r_max:
                    r_max = height[r]
                else:
                    answer += r_max - height[r]
                r -= 1
        return answer
