class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        dislike_graph = [list() for i in range(n + 1)]
        visited = [False for i in range(n + 1)]
        group = {}
        for dislike in dislikes:
            dislike_graph[dislike[0]].append(dislike[1])
            dislike_graph[dislike[1]].append(dislike[0])

        def dfs(i, group_num):
            if i in group and group_num != group[i]:
                return False

            group[i] = group_num
            if not visited[i]:
                visited[i] = True
                for dislike in dislike_graph[i]:
                    if dfs(dislike, 2 if group_num == 1 else 1) == False:
                        return False
            return True

        for i in range(1, n + 1):
            if not visited[i]:
                if dfs(i, 1) == False:
                    return False

        return True

