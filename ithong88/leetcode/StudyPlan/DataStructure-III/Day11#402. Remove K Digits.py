class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        cnt = 0
        stack = []
        for n in num:
            while stack and cnt < k and stack[-1] > n:
                stack.pop()
                cnt += 1

            if n != '0':
                stack.append(n)
            elif len(stack) > 0:
                stack.append(n)

        if cnt < k:
            stack = stack[0:(cnt - k)]

        return ''.join(stack) or '0'