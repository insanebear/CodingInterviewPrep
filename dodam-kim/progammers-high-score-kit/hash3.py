"""
https://programmers.co.kr/learn/courses/30/lessons/42578
"""


def solution(clothes):
    type_count = {}
    for item in clothes:
        if item[1] in type_count:
            type_count[item[1]] += 1
        else:
            type_count[item[1]] = 1

    answer = 1
    for item, count in type_count.items():
        answer *= count + 1
    answer -= 1

    return answer
