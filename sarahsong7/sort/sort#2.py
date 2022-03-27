def solution(numbers):
    answer = ''
    copy = []
    for n in enumerate(numbers):
        m=str(n[1])
        if len(m) < 4:
            r = 4-len(m)
            for index in range(r):
                m += m[index]
            #print(m)
        copy.append((m,n[0]))
        
    copy.sort(reverse=True)
    
    for c in copy:
        answer += str(numbers[c[1]])
    if int(answer) == 0:
        answer= '0'
    return answer