"""
<https://programmers.co.kr/learn/courses/30/lessons/42895>
"""

from itertools import product


def solution(N, number):
    representations = [[]]

    for count in range(1, 10):
        nnn = int(str(N) * count)
        if nnn == number:
            return count

        representations.append([int(str(N) * count)])

        for i in range(1, count):
            # lhs: representations[i]
            # rhs: representations[count - i]
            for lhs, rhs in product(representations[i], representations[count - i]):
                new_numbers = set(
                    [
                        lhs + rhs,
                        lhs * rhs,
                        abs(lhs - rhs),
                    ]
                )
                if rhs != 0:
                    new_numbers.add(lhs // rhs)

                if number in new_numbers:
                    return count

                representations[count].extend(new_numbers)
        representations[count] = set(representations[count])

    return -1
