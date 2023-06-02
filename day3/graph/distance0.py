from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def isvalid(row, col):
            if row >= len(mat) or row < 0 or col >= len(mat[0]) or col < 0:
                return False
            return True
        
        # get every zero and add them to a queue
        q = deque()
        visited = set()
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    q.append([row, col])
                    visited.add((row, col))
        
        level = 1 # the distance to the nearest zero starts from 1
        while q:
            size = len(q)
            for _ in range( size ):
                row, col = q.popleft()
                for r, c in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    newRow, newCol = row + r, col + c
                    if (newRow, newCol) not in visited and isvalid(newRow, newCol):
                        mat[newRow][newCol] = level
                        q.append([newRow, newCol])
                        visited.add((newRow, newCol))
            level += 1
        
        return mat