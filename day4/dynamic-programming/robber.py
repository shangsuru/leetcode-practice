from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        def robInner(robbedPrev: bool, i: int, money: int) -> int:
            if i >= len(nums):
                return money
            if robbedPrev:
                return robInner(False, i + 1, money)
            
            return max(
                robInner(True, i + 1, money + nums[i]),
                robInner(False, i + 1, money)
            )
        
        return robInner(False, 0, 0)