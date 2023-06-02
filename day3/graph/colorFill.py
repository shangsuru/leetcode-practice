from collections import deque
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        visited = set()
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        target = image[sr][sc]

        if target == color:
            return image

        def traverse(i, j):
            queue = deque([(i, j)])
            while queue:
                curr_i, curr_j = queue.popleft()
                if (curr_i, curr_j) not in visited:
                    visited.add((curr_i, curr_j))
                    image[curr_i][curr_j] = color
                    # Traverse neighbors.
                    for direction in directions:
                        next_i = curr_i + direction[0]
                        next_j = curr_j + direction[1]
                        if 0 <= next_i < rows and 0 <= next_j < cols:
                            if image[next_i][next_j] == target:
                                queue.append((next_i, next_j))
        
        traverse(sr, sc)
        return image

print(Solution().floodFill([[0,0,0],[1,0,0]], 1, 0, 2))