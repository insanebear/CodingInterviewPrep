class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda point: (point[0], point[1]))
        answer = 1
        left = 0
        right = sys.maxsize
        for l, r in points:
            # print(l, r, left, right, answer)
            if l > right:
                answer += 1
                left = l
                right = r
                continue

            if right > r:
                right = r
            if left < l:
                left = l
        return answer