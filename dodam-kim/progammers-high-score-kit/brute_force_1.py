"""
<https://programmers.co.kr/learn/courses/30/lessons/42840>
"""


def solution(answers):
    students = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
    ]

    scores = [0, 0, 0]
    for num, ans in enumerate(answers):
        for i in range(3):
            if ans == students[i][num % len(students[i])]:
                scores[i] += 1

    max_score = max(scores)
    answer = [i + 1 for i in range(len(scores)) if scores[i] == max_score]
    return answer
