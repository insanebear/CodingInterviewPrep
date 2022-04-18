def solution(number, k):
    answer = ''
    cnt = 0
    i = 0
    while i < len(number) - 1 and cnt < k:
        # print(f'i:{i}, number[i]:{number[i]}, number[i+1]:{number[i+1]}, number:{number}')
        if number[i] < number[i + 1]:
            number = number[:i] + number[i + 1:]
            cnt += 1
            if i > 0:
                i -= 1
        else:
            i += 1

    answer = number
    if cnt != k:
        answer = number[:-(k - cnt)]

    return answer

#     for i in range(k):
#         for j in range(len(number)-1):
#             if number[j] < number [j+1]:
#                 number = number[:j] + number[j+1:]
#                 cnt += 1
#                 break