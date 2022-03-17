def solution(clothes):
    answer = 1
    dic = dict()
    for clothe in clothes:
        if dic.get(clothe[1]) == None:
            dic[clothe[1]] = [clothe[0]]
        else:
            dic[clothe[1]].append(clothe[0])
    for key in dic.keys():
        answer *= (len(dic[key])+1)

    return answer-1