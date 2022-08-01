class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = dict() # adj list with cost
        for i in range(n):
            g[i] = dict()
        
        for s, d, c in flights:
            g[s][d] = c
        
        
        # best number of stops(distance) from src to i
        best_dist = [float("inf")] * n
        
        # (cost, node, distance)
        q = [(0, src, 0)]
        
        while q:
            cost, node, dist = heapq.heappop(q) # min cost
            print(cost, node, dist)
            # check if current is destination
            if node == dst:
                return cost
            
            # compare current to best_dist
            if best_dist[node] < dist: 
                continue
            
            # compare current to limit k -- check after checking destination
            if dist > k:
                continue
            
            # else,
            best_dist[node] = dist
            for neighbor, n_cost in g[node].items():
                heapq.heappush(q, (cost + n_cost, neighbor, dist + 1))
        return -1