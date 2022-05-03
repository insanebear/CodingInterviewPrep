class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        sp = 0
        answer = []
        
        for fl in firstList:
            print(fl)
            while sp < len(secondList):
                print(sp)
                if fl[0] <= secondList[sp][0] and fl[1] >= secondList[sp][0] and fl[1] <secondList[sp][1]:
                    temp = [secondList[sp][0],fl[1]]
                    answer.append(temp)
                    break
                elif fl[0] <= secondList[sp][0] and fl[1] >= secondList[sp][0] and fl[1] >= secondList[sp][1]:
                    temp = [secondList[sp][0],secondList[sp][1]]
                    answer.append(temp)
                    sp = sp+1
                elif fl[0] > secondList[sp][0] and fl[0] <= secondList[sp][1] and fl[1] >= secondList[sp][1]:
                    temp = [fl[0], secondList[sp][1]]
                    answer.append(temp)
                    sp = sp+1
                elif fl[0] > secondList[sp][0] and fl[0] <= secondList[sp][1] and fl[1] < secondList[sp][1]:
                    temp = [fl[0], fl[1]]
                    answer.append(temp)
                    break
                elif fl[0] > secondList[sp][1]:
                    sp = sp+1
                elif fl[1] < secondList[sp][0]:
                    break
                
        return answer
                