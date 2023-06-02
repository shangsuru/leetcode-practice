from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowsWith0 = set()
        colsWith0 = set()

        # find rows and columns that have a zero
        for i, rows in enumerate(matrix):
            for j, cell in enumerate(rows):
                if cell == 0:
                    rowsWith0.add(i)
                    colsWith0.add(j)

        # set those rows and cols to 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rowsWith0 or j in colsWith0:
                    matrix[i][j] = 0
        
        