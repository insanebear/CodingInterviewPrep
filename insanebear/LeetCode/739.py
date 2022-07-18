class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        ans = [0 for _ in range(l)]
        stack = []
        
        for i in range(l):
            current = temperatures[i]
            while stack and current > temperatures[stack[-1]]: # while stack exists and current is higher than top
                e = stack.pop() # continuously pop
                ans[e] = i-e # calcuate the gap
            stack.append(i) # add current
        
        return ans