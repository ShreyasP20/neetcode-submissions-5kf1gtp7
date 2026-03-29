class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.NumMatrix = matrix #[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        min_row = row1
        min_col = col1
        max_row = row2
        max_col = col2
        final_sum = 0
        for i in range(min_row, max_row+1):
            row1 = self.NumMatrix[i][min_col:max_col+1]
            final_sum += sum(row1)
        
        return final_sum
    




# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)