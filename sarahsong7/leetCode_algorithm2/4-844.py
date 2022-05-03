class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s = reversed(s)
        t = reversed(t)
        sn = 0
        news = ''; newt = ''
        for c in s:
            if c == '#':
                sn = sn+1
            elif c != '#' and sn <= 0:
                news=news+c
            else:
                sn = sn-1
        # print(news, sn)
        sn = 0
        for c in t:
            if c == '#':
                sn = sn+1
            elif c != '#' and sn <= 0:
                newt=newt+c
            else:
                sn = sn-1
        # print(newt, sn)
        if news == newt:
            return True
        return False