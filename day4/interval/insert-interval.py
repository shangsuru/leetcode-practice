from typing import List

class Solution:
    def overlaps(self, a: List[int], b: List[int]) -> bool:
        return a[0] <= b[1] and b[0] <= a[1]

    def merge(self, a: List[int], b: List[int]) -> List[int]:
        return [min(a[0], b[0]), max(a[1], b[1])]

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        inserted = False
        
        for i in intervals:
            if self.overlaps(newInterval, i):
                newInterval = self.merge(newInterval, i)
            else:
                if newInterval[1] < i[0]:
                    ans.append(newInterval) 
                    inserted = True
                ans.append(i)

        if not inserted:
            ans.append(newInterval)
        
        return ans