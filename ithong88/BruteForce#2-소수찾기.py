from itertools import permutations


def solution(numbers):
    answer = 0

    # make permutations
    permutation = list(permutations(numbers))
    for i in range(1, len(numbers)):
        permutation += list(permutations(numbers, i))

    # make numbers from permutations
    number_set = set()
    for item in permutation:
        number = ''
        for x in item:
            number += x
        if int(number) == 0 or int(number) == 1:
            continue
        number_set.add(int(number))

    # check if number is prime or not
    for number in number_set:
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            answer += 1

    return answer