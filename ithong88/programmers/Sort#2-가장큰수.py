def solution(numbers):
    answer = ''
    # Ver.1
    # numbers = [3, 30, 33, 34, 300, 333, 321, 345, 1000, 77, 22, 0]
    # numbers = [9, 998]
    #     strings = [str(number) for number in numbers]

    # #     3 30
    # #     33 30
    # #     330 > 303

    #     sorted_strings = sorted(strings, key=lambda string: (string[0],
    #                                                          string[min(1, len(string)-1)],
    #                                                          string[min(2, len(string)-1)],
    #                                                          string[min(3, len(string)-1)]), reverse=True)
    #     # print(sorted_strings)
    #     for string in sorted_strings:
    #         answer += string

    # Ver.2
    strings = [[str(number), str(number) * 3] for number in numbers]
    # print(strings)
    sorted_strings = sorted(strings, key=lambda string: string[1], reverse=True)
    # print(sorted_strings)
    for string in sorted_strings:
        answer += string[0]

    if int(answer) == 0:
        answer = '0'
    # print(answer)
    return answer