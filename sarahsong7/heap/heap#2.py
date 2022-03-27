# import heapq
# def solution(jobs):
#     answer = 0
#     length = len(jobs)
    
#     heapq.heapify(jobs)
#     time = 0
#     node = heapq.heappop(jobs)
#     if node[0] > time:
#         time = node[0]+node[1]
#     else:
#         time += node[1]
#     answer += (time - node[0])
        
# #     while jobs:
# #         temp_list = []
# #         while jobs:
# #             node = heapq.heappop(jobs)
# #             if node[0] < time:
# #                 temp_list.append(node)
# #             else:
# #                 heapq.heappush(jobs, node)
# #                 break
    
# #         temp_list.sort(key=lambda x: (x[1],x[0]))
# #         smallest = temp_list.pop(0)
# #         if smallest[0] > time:
# #             time = smallest[0]+smallest[1]
# #         else:
# #             time += smallest[1]
# #         answer += (time - smallest[0])
# #         print(answer)
# #         for temp in temp_list:
# #             heapq.heappush(jobs, temp)

#     while jobs:
#         temp_list = []
#         while jobs:
#             node = heapq.heappop(jobs)
#             if node[0] < time:
#                 heapq.heappush(temp_list,(node[1],node[0]))
#             else:
#                 heapq.heappush(jobs, node)
#                 break
    
#         # temp_list.sort(key=lambda x: (x[1],x[0]))
#         smallest = temp_list.pop(0)
#         if smallest[1] > time:
#             time = smallest[0]+smallest[1]
#         else:
#             time += smallest[0]
#         answer += (time - smallest[1])
#         # print(answer)
#         for temp in temp_list:
#             heapq.heappush(jobs, [temp[1],temp[0]])
    
#     return answer//length

def solution(jobs):
    from heapq import heappush, heappop
    import operator

    current = 0
    answer = 0

    l = len(jobs)
    # sort jobs by request time 
    jobs = sorted(jobs, key=operator.itemgetter(0, 1))

    waitings = []
    heappush(waitings, (0, jobs.pop(0)))

    while waitings:

        processing = heappop(waitings)[1]

        if processing[0] > current:
            current = processing[0] + processing[1]
        else:
            current += processing[1]

        answer += (current - processing[0])

        while True:
            if jobs and jobs[0][0] < current:
                heappush(waitings, (jobs[0][1], jobs[0]))
                jobs.pop(0)
            else:
                if jobs and len(waitings) == 0:

                    # loop until task with different start time 
                    prev = jobs[0][0]
                    while jobs:
                        job = jobs[0]

                        if job[0] != prev:
                            break

                        heappush(waitings, (job[1], job))
                        prev = job[0]
                        jobs.pop(0)

                break
    answer //= l

    return answer