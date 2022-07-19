class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        answer = [0]*length
        if length == 1:
            return [0]
        stack = []
        for i in range(0,length):
            if stack!= []:
                # print(stack)
                while temperatures[i] > stack[-1][0]:
                    answer[stack[-1][-1]] = i-stack[-1][-1]
                    stack.pop()
                    if stack == []:
                        break
            stack.append([temperatures[i],i])
        return answer