import heapq

def solution(operations):
    min_pq = []
    max_pq = []
    
    for op in operations:
        command, value = op.split()
        if command == "I":
            # insert
            heapq.heappush(min_pq, int(value))
            heapq.heappush(max_pq, -int(value))
        elif command == "D":
            if len(min_pq) == 0:
                continue
                
            if value == "-1":
                # pop min
                idx = max_pq.index(-heapq.heappop(min_pq))
                del max_pq[idx]
                heapq.heapify(max_pq)
            else:
                # pop max
                idx = min_pq.index(-heapq.heappop(max_pq))
                del min_pq[idx]
                heapq.heapify(min_pq)
    
    return [max(min_pq), min(min_pq)] if len(min_pq) != 0 else [0, 0]