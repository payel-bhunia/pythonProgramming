class Solution:
    def generateMatrix(self, A):
        roww = [1] * A
        matrix = []
        for i in range(A):
            matrix.append(roww.copy())
        row = 0
        col = 0
        val = 1
        mat = A
        ans = []
        while mat > 1:
            i = row
            for j in range(mat-1):
                matrix[i][j+col] = val
                val += 1
            j = A - 1 - col
            for i in range(mat-1):
                matrix[i+row][j] = val
                val += 1
            i = A - 1 - row
            for j in range(A - 1 - col, col, -1):
                matrix[i][j] = val
                val += 1
            j = col
            for i in range(A - 1 - row, row, -1):
                matrix[i][j] = val 
                val += 1
            mat -= 2
            row += 1
            col += 1
        if mat == 1:
            matrix[row][mat-1+col] = val
        return matrix

s = Solution()
ans = s.generateMatrix(21)
print(ans)