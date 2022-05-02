class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        answer = []

        # path = []

        def dfs(graph, cur, path=[], answer=[]):
            # termination condition
            if cur == len(graph) - 1:
                path.append(cur)
                answer.append(path)
                return

            for next in graph[cur]:
                new_path = path[:]
                new_path.append(cur)

                dfs(graph, next, new_path, answer)

        dfs(graph, 0, [], answer)
        return answer

