import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        first_min = heapq.heappop(scoville)
        secon_min = heapq.heappop(scoville)
        heapq.heappush(scoville, first_min+secon_min*2)
        answer += 1
        if scoville[0] >= K:
            break
        if len(scoville) == 1:
            answer = -1
            break
    return answer