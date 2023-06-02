from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []

        # borders
        rowEnd = len(matrix)
        colEnd = len(matrix[0])
        rowStart = 0
        colStart = 0

        while rowStart < rowEnd and colStart < colEnd:
            
            # go right
            for i in range(colStart, colEnd):
                ans.append(matrix[rowStart][i])
            
            if rowStart + 1 == rowEnd:
                break
            # go down
            for i in range(rowStart + 1, rowEnd):
                ans.append(matrix[i][colEnd - 1])

            # go left
            for i in range(colEnd - 2, colStart - 1, -1):
                ans.append(matrix[rowEnd - 1][i])

            if colStart + 1 == colEnd:
                break
            # go up
            for i in range(rowEnd - 2, rowStart, -1):
                ans.append(matrix[i][colStart])

            # update borders
            rowEnd -= 1
            colEnd -= 1
            rowStart += 1
            colStart += 1

        return ans