class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowL = 0
        rowR = len(matrix)-1
        rowM = 0
        colN = len(matrix[0])
        while rowL < rowR:
            rowM = (rowL+rowR)//2
            print(rowL,rowM, rowR)
            if matrix[rowL][colN-1] >= target:
                rowM = rowL
                break
            elif matrix[rowL][colN-1] < target and matrix[rowR][0] > target and matrix[rowM][colN-1] >= target:
                rowR = rowM
            elif matrix[rowL][colN-1] < target and matrix[rowR][0] > target and matrix[rowM][colN-1] < target:
                rowL = rowM+1
            elif matrix[rowR][0] <= target:
                rowM = rowR
                break
        
        print(rowM)
        if matrix[rowM][colN-1] == target:
            return True
        if matrix[rowM][0] == target:
            return True
        
        colL = 0
        colR = colN-1
        colM = 0
        while colL < colR:
            colM = (colL+colR)//2
            # print(colL, colM, colR)
            if matrix[rowM][colL] > target:
                return False
            elif matrix[rowM][colL] <= target and matrix[rowM][colR] >= target and matrix[rowM][colM] > target:
                # colL = colM
                colR = colM
            elif matrix[rowM][colL] <= target and matrix[rowM][colR] >= target and matrix[rowM][colM] < target:
                colL = colM+1
                # print(colL,matrix[rowM][colM], colR)
            elif matrix[rowM][colL] <= target and matrix[rowM][colR] >= target and matrix[rowM][colM] == target:
                return True
            elif matrix[rowM][colR] < target:
                return False
        
        if matrix[rowM][colM] == target:
            return True
        
        return False