"""
<https://programmers.co.kr/learn/courses/30/lessons/42627>
"""

import heapq


def solution(jobs):
    job_count = len(jobs)
    heapq.heapify(jobs)
    ready_queue = []

    timestamp = 0
    total_time = 0

    while jobs or ready_queue:
        while jobs and jobs[0][0] <= timestamp:
            job = heapq.heappop(jobs)
            heapq.heappush(ready_queue, [job[1], job[0]])

        if ready_queue:
            exec_time, req_time = heapq.heappop(ready_queue)
            timestamp += exec_time
            total_time += timestamp - req_time
        elif jobs:
            timestamp = jobs[0][0]

    return total_time // job_count
