"""
<https://programmers.co.kr/learn/courses/30/lessons/42626>
"""

import heapq


def solution(scoville, K):
    heapq.heapify(scoville)

    answer = 0
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        mixed = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, mixed)
        answer += 1

    return answer
