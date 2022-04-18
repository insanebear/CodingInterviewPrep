import bisect
def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    left = 1; right = distance; mid = 0;
    
    while left <= right:
        prev = 0; cnt = 0
        mid = (left+right)//2
        for rock in rocks:
            if rock-prev < mid:
                cnt=cnt+1
            else:
                prev = rock
        
        if distance-prev<mid:
            cnt = cnt+1
        
        if cnt <= n:
            answer = max(answer,mid)
            left = mid+1
        else:
            right = mid-1
    
    return answer