"""
<https://programmers.co.kr/learn/courses/30/lessons/42747#>
"""


def solution(citations):
    citations.sort(reverse=True)

    for i, cite in enumerate(citations):
        if cite == (i + 1):
            return cite
        elif cite < (i + 1):
            return i

    return min(len(citations), citations[-1])
