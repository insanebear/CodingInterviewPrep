from collections import deque


def solution(tickets):
    graph = dict()
    for ticket in tickets:
        graph.setdefault(ticket[0], [0, []])
        graph.setdefault(ticket[1], [0, []])
        graph[ticket[0]][1].append(ticket[1])
        graph[ticket[1]][0] += 1

    for items in graph.values():
        items[1].sort()

    next_node = deque(["ICN"])

    answer = []
    while next_node:
        curr = next_node.popleft()
        answer.append(curr)

        if len(graph[curr][1]) == 0:
            break

        for cand in graph[curr][1]:
            if graph[cand][0] == 1:
                graph[cand][0] = 0
                next_node.append(cand)
                graph[curr][1].remove(cand)
                break
        if not next_node:
            cand = graph[curr][1][0]
            next_node.append(cand)
            graph[cand][0] -= 1
            graph[curr][1].remove(cand)

    return answer


# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets = [
    ["ICN", "SFO"],
    ["ICN", "ATL"],
    ["SFO", "ATL"],
    ["ATL", "ICN"],
    ["ATL", "SFO"],
]
print(solution(tickets))
