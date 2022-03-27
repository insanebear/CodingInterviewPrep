"""
<https://programmers.co.kr/learn/courses/30/lessons/42746>
"""


def solution(numbers):
    str_nums = [str(n) for n in numbers]
    str_nums.sort(key=lambda n: n * 3, reverse=True)

    answer = ""
    for num in str_nums:
        answer += num

    return answer if answer[0] != "0" else str(0)
