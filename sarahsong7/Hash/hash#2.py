def solution(phone_book):
    dic = dict()
    for phone_number in phone_book:
        dic[phone_number] = 1
    
    for phone_number in phone_book:
        for i in range(len(phone_number)):
            if dic.get(phone_number[0:i]) != None:
                answer = False
                return answer

    answer = True
    return answer