class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        visited = [0] * len(isConnected)
        # print(visited)
        queue = []

        for i in range(len(isConnected)):
            if visited[i] == 0:
                queue.append(i)

                while queue:
                    cur = queue.pop()
                    visited[cur] = 1

                    for j in range(len(isConnected)):
                        if isConnected[cur][j] == 1 and visited[j] == 0:
                            queue.append(j)

                provinces += 1

        return provinces