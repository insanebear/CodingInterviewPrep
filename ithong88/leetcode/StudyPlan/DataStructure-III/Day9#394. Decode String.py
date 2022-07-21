from collections import deque


class Solution:
    def decodeString(self, s: str) -> str:
        n_q = deque()
        s_q = deque()
        temp_n = 0
        temp_s = ''
        answer = ''
        for c in s:
            if c.isnumeric():
                temp_n = 10 * temp_n + int(c)
            elif c == '[':
                n_q.append(temp_n if temp_n != 0 else 1)
                s_q.append(temp_s)
                temp_n = 0
                temp_s = ''
            elif c == ']':
                temp_s = s_q.pop() + n_q.pop() * temp_s
            else:
                temp_s = temp_s + c
        return temp_s

