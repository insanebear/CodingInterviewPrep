# # Ver.1
# class Solution:
#     def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
#         i, j = 0, 0
#         answer = []
#         while i < len(firstList) and j < len(secondList):
#             fs, fe, ss, se = firstList[i][0], firstList[i][1], secondList[j][0], secondList[j][1]
#
#             # no intersection - first before second
#             if fe < ss:
#                 i += 1
#                 # no intersection - first after second
#             elif fs > se:
#                 j += 1
#                 # first contains second
#             elif fs <= ss and fe >= se:
#                 answer.append([ss, se])
#                 j += 1
#             # second contains first
#             elif fs >= ss and fe <= se:
#                 answer.append([fs, fe])
#                 i += 1
#             # start with first, end with second
#             elif fs <= ss and fe <= se:
#                 answer.append([ss, fe])
#                 i += 1
#             # start with second, end with first
#             elif fs >= ss and fe >= se:
#                 answer.append([fs, se])
#                 j += 1
#             else:
#                 pass
#
#         return answer

# Ver.2
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        answer = []
        while i < len(firstList) and j < len(secondList):
            fs, fe, ss, se = firstList[i][0], firstList[i][1], secondList[j][0], secondList[j][1]

            start = max(fs, ss)
            end = min(fe, se)

            if start <= end:
                answer.append([start, end])

            if end == fe:
                i += 1
            else:
                j += 1

        return answer