# Ver.1
# def solution(phone_book):
#     answer = True
#     dic = dict()
#     # print(dic)
#     for number in phone_book:
#         for i in range(len(number)-1):
#             key = number[:i+1]
#             dic[key] = 1

#     for number in phone_book:
#         if number in dic:
#             return False
#     return answer


# Ver.2
def solution(phone_book):
    print('#1');
    for i in range(len(phone_book)):
        print(phone_book[i])
    print()
    print('#2')
    for phone_number in phone_book:
        print(phone_number)
    print()
    print('#3')
    for i, phone_number in enumerate(phone_book):
        print(f'idx:{i}, phone_number:{phone_number}')

        # print('idx:' + i + ', ')

    answer = True
    #     dic = dict()
    #     for number in phone_book:
    #         dic[number] = 1

    #     for number in phone_book:
    #         for i in range(len(number)-1):
    #             key = number[:i+1]
    #             if key in dic:
    #                 return False
    return answer