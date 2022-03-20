def solution(progresses, speeds):
    answer = []
    update = 0
    isEnd = False
    for day in range(1,101):
        for i,progress in enumerate(progresses):
            progresses[i] += speeds[i]
        if progresses[update]>=100:
            for i,progress in enumerate(progresses):
                if progress < 100 and i != update:
                    answer.append(i-update)
                    update = i
                    break
                if progress >= 100 and i == len(progresses)-1:
                    answer.append(len(progresses)-update)
                    isEnd = True
        if isEnd:
            break

    return answer