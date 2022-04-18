# Ver.2
def solution(participant, completion):
    answer = ''
    dictionary = dict()
    for part in participant:
        dictionary[part] = dictionary.get(part, 0) + 1

    for comp in completion:
        cnt = dictionary[comp]
        if cnt == 1:
            del dictionary[comp]
        else:
            dictionary[comp] -= 1

    answer = list(dictionary.keys())[0]

    return answer

# Ver.1
# def solution(participant, completion):
#     answer = ''

#     # ans = set(participant) - set(completion)

#     dictionary = dict()
#     # Key : 이름, Value : count
#     for part in participant:
#         if part in dictionary:
#             cnt = dictionary[part]
#             cnt = cnt + 1
#             dictionary[part] = cnt
#         else:
#             dictionary[part] = 1

#     for comp in completion:
#         cnt = dictionary[comp]
#         if cnt == 1:
#             del dictionary[comp]
#         else:
#             cnt = cnt - 1
#             dictionary[comp] = cnt

#     # for ans in dictionary:
#     #     answer = ans
#     print(dictionary.keys())
#     answer = list(dictionary.keys())[0]

#     # print(dictionary)

#     return answer


# Others
# import collections


# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]