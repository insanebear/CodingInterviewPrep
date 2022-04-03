import itertools
from math import floor, sqrt

"""
<https://programmers.co.kr/learn/courses/30/lessons/42839>
"""


def solution(numbers):
    def is_prime(num: int):
        if num <= 1:
            return False
        if num in [2, 3]:
            return True
        for i in range(2, floor(sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    prime_set = set()
    for length in range(1, len(numbers) + 1):
        for cand in itertools.permutations(numbers, length):
            num = int("".join(cand))

            if is_prime(num):
                prime_set.add(num)

    return len(prime_set)
