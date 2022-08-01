class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [] # monotonic decreasing
        num_k = -float('inf')
        # 1-3-2
        for n in nums[::-1]:
            if n < num_k:
                return True
            while stack and stack[-1] < n:
                num_k = stack.pop()
            stack.append(n)
        
        return False