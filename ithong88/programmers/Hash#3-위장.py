def solution(clothes):
    answer = 1
    closet = {}
    for item in clothes:
        temp = closet.get(item[1], [])
        if temp == []:
            closet[item[1]] = [item[0]]
        else:
            temp.append(item[0])

    for item in closet:
        answer = answer * (len(closet[item]) + 1)
        # print(item)

    answer = answer - 1

    return answer