from typing import List

class Solution:
    def overlaps(self, a: List[int], b: List[int]) -> bool:
        return a[0] <= b[1] and b[0] <= a[1]

    def mergeTwo(self, a: List[int], b: List[int]) -> List[int]:
        return [min(a[0], b[0]), max(a[1], b[1])]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda l:l[0])
        ans = []

        i = 0
        j = 1
        while j < len(intervals):
            if self.overlaps(intervals[i], intervals[j]):
                merged = self.mergeTwo(intervals[i], intervals[j])
                intervals[j] = merged
            else:
                ans.append(intervals[i])
            i += 1
            j += 1
        if i < len(intervals):
            ans.append(intervals[i])

        return ans



