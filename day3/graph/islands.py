from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def traverse(i: int, j: int) -> None:
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return 0
            if grid[i][j] != "1":
                return 0
            
            grid[i][j] = "2"
            for d in directions:
                traverse(i + d[0], j + d[1])
            return 1
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                islands += traverse(i, j)


        return islands