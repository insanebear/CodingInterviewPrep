class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:(x[0],x[1]))
        answer = 0
        loc = 0
        last = points[0][1]
        # print(points)
        for i,p in enumerate(points):
            # print("crit", points[loc][1])
            if last < p[0]:
                # print(p, last, "last")
                loc = i
                last = p[1]
                answer = answer + 1
                continue
                
            if p[0] <= points[loc][1] and p[1] >= last:
                # print(p,"skip")
                continue
            elif p[0] <= points[loc][1] and p[1] < last:
                last = p[1]
            else:
                # print(p,"plus")
                last = p[1]
                loc = i
                answer = answer + 1
                
        answer = answer + 1
        
        return answer