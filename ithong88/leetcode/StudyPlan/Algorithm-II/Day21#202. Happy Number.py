class Solution:
    def isHappy(self, n: int) -> bool:
        answer = n
        cnt = 0
        history = set()
        while answer not in history:
            history.add(answer)
            temp = 0
            s = str(answer)
            for c in s:
                temp += int(c) * int(c)
            answer = temp
            if answer == 1:
                return True
        return False
