from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = 1
        maxDp = 1
        for i in range(1, len(nums)):
            maxI = 0
            for j in range(0, i):
                if nums[i] > nums[j]:
                    maxI = max(dp[j], maxI)
            dp[i] = maxI + 1
            maxDp = max(maxDp, dp[i])

        return maxDp