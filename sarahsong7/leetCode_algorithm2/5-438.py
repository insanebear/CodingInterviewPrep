class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        answer = []
#         q = ''.join(sorted(p))
        
#         for i in range(0,len(s)-len(p)+1):
#             temp = s[i:i+len(p)]
#             temp = sorted(temp)
#             if ''.join(temp) == q:
#                 answer.append(i)
        oracle = [0 for i in range(26)]
        slide = [0 for i in range(26)]
        for i in p:
            oracle[ord(i)-ord('a')]= oracle[ord(i)-ord('a')]+1
        oo = map(str,oracle)
        o = int(''.join(oo))
        # print(o)
        
        for i in s[0:len(p)]:
            slide[ord(i)-ord('a')]= slide[ord(i)-ord('a')]+1
        ss = map(str,slide)
        s_int = int(''.join(ss))
        # print(s_int)
        
        if o^s_int == 0:
            answer.append(0)
            
        for i in range(0,len(s)-len(p)):
            slide[ord(s[i])-ord('a')] = slide[ord(s[i])-ord('a')]-1
            slide[ord(s[i+len(p)])-ord('a')] = slide[ord(s[i+len(p)])-ord('a')]+1

            if slide[ord(s[i])-ord('a')] == oracle[ord(s[i])-ord('a')] and slide[ord(s[i+len(p)])-ord('a')] == oracle[ord(s[i+len(p)])-ord('a')]:
                ss = map(str,slide)
                s_int = int(''.join(ss))
                if o^s_int == 0:
                    answer.append(i+1)
        
        return answer