"""
<https://programmers.co.kr/learn/courses/30/lessons/42842>
"""


def solution(brown, yellow):
    """
    Conditions
    1. y_x >= y_y
    2. y_x * y_y = yellow
    3. 2 * (y_x + y_y) + 4 = brown
    """
    for y_col in range(1, yellow + 1):
        y_row = yellow // y_col
        if (
            (y_row * y_col) == yellow
            and 2 * (y_row + y_col) + 4 == brown
            and y_row >= y_col
        ):
            return [y_row + 2, y_col + 2]

    return []
