def solution(priorities, location):
    answer = 0
    target = priorities[location]
    index = list(range(len(priorities)))
    # print(index)
    queue = priorities.copy()
    queue.sort(reverse=True)

    priority_queue = priorities

    print(queue)
    cnt = 1
    while (True):
        # for priority in priorities:
        if priority_queue[0] == queue[0]:
            # print(f'priority_queue:{priority_queue[0]}, queue:{queue[0]}')
            if index[0] == location:
                print(cnt)
                return cnt
            else:
                priority_queue.pop(0)
                index.pop(0)
                queue.pop(0)
                cnt += 1
            # print(priority_queue)
            # print(index)
        else:
            priority_queue.append(priority_queue[0])
            priority_queue.pop(0)
            index.append(index[0])
            index.pop(0)
            # print(priority_queue)
            # print(index)

    return answer