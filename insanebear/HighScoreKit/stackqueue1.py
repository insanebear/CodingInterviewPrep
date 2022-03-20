import math

def solution(progresses, speeds):
    answer = []
    days = []

    # calculate how many days are needed to complete
    for i, p in enumerate(progresses): # O(n)
        days.append(math.ceil((100 - p) / speeds[i]))
    
    count = 0
    done = days[0] # date to complete the first front job in a queue
    
    for d in days: # O(n)
        # `day` is less than equal to done
        if d <= done: 
            # `day` has been done already.
            count += 1
        else:
        # `day` is greater than done
            answer.append(count) # append the calculated count so far
            done = d    # set done to `day`
            count = 1   # reset count
    answer.append(count)
    return answer