import heapq

def solution(scoville, K):
    answer = 0

    # build a min heap
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        # nothing left to mix
        if len(scoville) == 1:
            return -1
        
        # mix
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new_scoville = first + 2*second
        heapq.heappush(scoville, new_scoville)
        answer += 1
        
    return answer