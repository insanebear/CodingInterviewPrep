class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        print()
        paths = []
        recur([0], 0, paths, graph)
        return paths

def recur(path, index, paths, graph):
    # end condition
    if len(graph)-1 == index:
        # print(path)
        paths.append(path)
        return;
        
    # newPath = path
    # print(graph[index])
    for n in graph[index]:
        newPath = path.copy()
        newPath.append(n)
        # print('newPath: '+str(newPath))
        recur(newPath, n, paths, graph)
    
    
    