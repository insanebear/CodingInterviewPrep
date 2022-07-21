class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        answer = set()
        candidates = set()
        for i in range(len(s)-9):
            ss = s[i:i+10]
            if ss in candidates:
                answer.add(ss)
            else:
                candidates.add(ss)
        # print(answer)
        # print(candidates)
        return list(answer)