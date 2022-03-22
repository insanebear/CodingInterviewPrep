"""
<https://programmers.co.kr/learn/courses/30/lessons/42584>
- keep stocks whose price hasn't been decreased yet, within the stock
"""


def solution(prices):
    answer = list(range(len(prices)))
    answer.reverse()

    stack = []
    for price in enumerate(prices):
        while stack and (stack[-1][1] > price[1]):
            index = stack.pop()[0]
            answer[index] = price[0] - index

        stack.append(price)

    return answer
