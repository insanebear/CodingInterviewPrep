class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        f_len, s_len = len(firstList), len(secondList)
        i, j = 0, 0
        answers = []
        while i < f_len and j < s_len:
            A, B = firstList[i], secondList[j]
            A_start, A_end = A[0], A[1]
            B_start, B_end = B[0], B[1]
            
            # Check intersection
            if A_start <= B_start and B_start <= A_end and A_end <= B_end:
                answers.append([B_start, A_end])
            elif A_start < B_start and B_end < A_end:
                answers.append([B_start, B_end])
            elif B_start <= A_start and A_start <= B_end and B_end <= A_end:
                answers.append([A_start, B_end])
            elif B_start < A_start and A_end < B_end:
                answers.append([A_start, A_end])
            
            # Move pointer
            if A_end == B_end:
                i += 1
                j += 1
            elif A_end < B_end:
                i += 1
            elif B_end < A_end:
                j += 1
        
        return answers