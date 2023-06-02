from heapq import heappush, heappushpop
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for id, p in enumerate(points):
            d = p[0] * p[0] + p[1] * p[1]
            if len(maxHeap) < k:
                heappush(maxHeap, (-d, id))
            else:
                heappushpop(maxHeap, (-d, id))

        return [points[id] for _, id in maxHeap]      