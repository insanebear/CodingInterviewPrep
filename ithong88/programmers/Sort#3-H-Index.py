def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i, citation in enumerate(citations):
        if citation > i:
            answer = i + 1

    return answer