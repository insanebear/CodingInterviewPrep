def solution(participant, completion):
    dic = dict()
    for part in participant:
        if dic.get(part) == None:
            dic[part]=1
        else:
            dic[part]+=1
    
    for com in completion:
        if dic.get(com) == 1:
            dic.pop(com)
        else:
            dic[com]-=1
    
    for part in dic.keys():
        return part
    answer = ''
    return answer