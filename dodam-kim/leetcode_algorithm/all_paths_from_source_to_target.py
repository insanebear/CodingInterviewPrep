"""
<https://leetcode.com/problems/all-paths-from-source-to-target/>
"""

from typing import List

# 1st approach
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # graph: adj_list --> graph[n]: [neighbors of n]
        # source = 0
        dest = len(graph) - 1

        path_stack = [[0]]
        paths = []
        seen_nodes = set()

        while path_stack:
            path = path_stack.pop()
            seen_nodes = set(path)
            last = path[-1]
            if last == dest:
                paths.append(path)

            for cand in graph[last]:
                if cand not in seen_nodes:
                    path_stack.append(path + [cand])

        return paths


# 2nd approach: no need to keep 'seen' nodes
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # graph: adj_list --> graph[n]: [neighbors of n]
        # source = 0
        dest = len(graph) - 1

        path_stack = [[0]]
        paths = []

        while path_stack:
            path = path_stack.pop()
            last = path[-1]
            if last == dest:
                paths.append(path)

            for cand in graph[last]:
                path_stack.append(path + [cand])

        return paths
