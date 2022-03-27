def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if i+1 >= citations[i]:
            return citations[i]
        elif i+1 != len(citations):
            temp = citations[i]
            while citations[i+1] < temp:
                temp -= 1
                if i+1 >= temp:
                    return temp
        elif i+1 == len(citations):
            temp = citations[i]-1
            while True:
                if i+1 >= temp:
                    return temp
                temp -= 1
    return answer