def solution(numbers, target):
    answer = [0]

    def dfs(i, sum, answer):
        if i == len(numbers) and target == sum:
            answer[0] += 1
            return
        if i == len(numbers):
            return
        
        dfs(i+1, sum + numbers[i], answer)
        dfs(i+1, sum - numbers[i], answer)
        
    dfs(0, 0, answer)
        
    return answer[0]