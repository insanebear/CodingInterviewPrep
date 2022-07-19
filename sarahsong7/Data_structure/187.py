class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dic = dict()
        for i in range(0,len(s)-9):
            dic.setdefault(s[i:i+10],0)
            dic[s[i:i+10]] += 1
        
        answer = []
        for key in dic.keys():
            if dic[key] > 1:
                answer.append(key)
                
        return answer