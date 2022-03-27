# Ver.1
def solution(n, lost, reserve):
    answer = 0

    for i in range(1, n + 1):
        if i in lost:
            if i in reserve:
                lost.remove(i)
                reserve.remove(i)

    for i in range(1, n + 1):
        if i in lost:
            if (i-1) in reserve:
                lost.remove(i)
                reserve.remove(i-1)
            elif (i+1) in reserve:
                lost.remove(i)
                reserve.remove(i+1)

    answer = n - len(lost)
    return answer

## Ver.2
# def solution(n, lost, reserve):
#     answer = 0
#
#     lost_copy = lost[:]
#
#     for i in lost_copy:
#         if i in reserve:
#             lost.remove(i)
#             reserve.remove(i)
#     lost.sort()
#     reserve.sort()
#
#     lost_copy = lost[:]
#     for i in lost_copy:
#         if (i - 1) in reserve:
#             lost.remove(i)
#             reserve.remove(i - 1)
#         elif (i + 1) in reserve:
#             lost.remove(i)
#             reserve.remove(i + 1)
#     answer = n - len(lost)
#     return answer