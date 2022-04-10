from itertools import product
from collections import deque

"""
<https://programmers.co.kr/learn/courses/30/lessons/43163>
"""


def solution(begin, target, words):
    # start, end: indices of begin, target
    try:
        end = words.index(target)
    except ValueError as v:
        return 0

    # make adj_list: 2-dim list
    # - is_connected: count(different character) == 1
    # - complexity: time O(words^2), space: O(words^2)
    # BFS to find the shortest path from begin to target
    # - complexity: time O(V + E) == (words^2),
    #               space O(V) == (words), for queue, visited mark each
    def is_connected(lhs, rhs):
        count = 0
        for l, r in zip(lhs, rhs):
            if l != r:
                count += 1
        return True if (count == 1) else False

    def build_graph():
        adj_list = [[] for _ in words]

        index = range(len(words))
        for left, right in product(index, index):
            if is_connected(words[left], words[right]):
                adj_list[left].append(right)
                adj_list[right].append(left)

        return adj_list

    adj_list = build_graph()

    def len_shortest_path(begin, end):
        node_queue = deque()
        dist = [0] * len(words)

        for i, word in enumerate(words):
            if is_connected(begin, word):
                node_queue.append(i)
                dist[i] = 1

        while deque:
            node = node_queue.popleft()
            if node == end:
                return dist[node]

            for cand in adj_list[node]:
                if dist[cand] == 0:
                    node_queue.append(cand)
                    dist[cand] = dist[node] + 1

        return 0

    return len_shortest_path(begin, end)
