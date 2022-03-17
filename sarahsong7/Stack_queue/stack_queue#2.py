def solution(priorities, location):
    answer = 0
    cl = 0
    while True:
        isPop = True
        for i in range(cl,len(priorities)):
            if priorities[cl]<priorities[i]:
                priorities.append(priorities[cl])
                if location == cl:
                    location = len(priorities)-1
                cl+=1
                isPop =False
                break
        if isPop:
            answer+=1
            if cl == location:
                break
            cl+=1
    
    return answer