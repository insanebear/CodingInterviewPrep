from collections import deque


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        queue = deque()
        answer = [0 for _ in temperatures]
        for i, temp in enumerate(temperatures):
            if i == 0:
                queue.append(i)
                continue
            while len(queue) > 0:
                idx = queue.pop()
                if temp > temperatures[idx]:
                    answer[idx] = i - idx
                else:
                    queue.append(idx)
                    break
            queue.append(i)

        return answer


