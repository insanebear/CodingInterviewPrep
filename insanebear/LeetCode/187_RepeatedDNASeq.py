class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        
        d = {}
        for i in range(len(s)-9):
            subseq = s[i:i+10]
            d[subseq] = d.get(subseq, 0) + 1
        
        ans = []
        for k, v in d.items():
            if v > 1:
                ans.append(k)
        
        return ans