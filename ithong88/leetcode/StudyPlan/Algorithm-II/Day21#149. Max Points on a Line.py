class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        lines = dict()
        answer = 0

        def getLinearFunction(p1, p2):
            y_diff = p1[1] - p2[1]
            x_diff = p1[0] - p2[0]
            a = 0
            b = 0
            if x_diff != 0:
                a = y_diff / x_diff
                b = p1[1] - p1[0] * a
                return (a, b, 0, 0, 'xy')
            elif x_diff == 0:\
                return (0, 0, p1[0], 0, 'x')
            elif y_diff == 0:
                return (0, 0, 0, p1[1], 'y')
            else:
                return (0, 0, 0, 0, 'error')

        for i in range(len(points)):
            for j in range(i, len(points)):
                f = getLinearFunction(points[i], points[j])
                temp = set()
                if f in lines:
                    temp = lines[f]
                    # else:
                #     temp = set()

                temp.add(tuple(points[i]))
                temp.add(tuple(points[j]))
                lines[f] = temp

                answer = max(answer, len(lines[f]))

        # print(lines)
        # for key in lines.keys():
        #     print(len(lines[key]), key, lines[key])

        return answer

