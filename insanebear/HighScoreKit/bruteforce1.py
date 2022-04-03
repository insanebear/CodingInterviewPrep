def solution(answers):
    answer = []
    counts = []
    students = [
        [1, 2, 3, 4, 5], 
        [2, 1, 2, 3, 2, 4, 2, 5], 
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    for student in students:
        count = 0
        for i, ans in enumerate(answers):
            if ans == student[i % len(student)]:
                count += 1
        counts.append(count)

    for s_id in range(len(students)):
        if max(counts) == counts[s_id]:
            answer.append(s_id+1)
            
    return answer