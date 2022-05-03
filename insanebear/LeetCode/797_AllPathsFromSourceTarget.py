class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        def dfs(node, path, paths):
            if node == len(graph)-1 :
                paths.append(path+[node])
            else:
                for next_node in graph[node]:
                    dfs(next_node, path+[node], paths)
        
        paths = []
        dfs(0, [], paths)
        
        return paths