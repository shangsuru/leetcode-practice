from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def searchRec(start: int, end: int) -> int:
            if start > end:
                return -1
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                return searchRec(start, mid - 1)
            if nums[mid] < target:
                return searchRec(mid + 1, end)

        return searchRec(0, len(nums) - 1)