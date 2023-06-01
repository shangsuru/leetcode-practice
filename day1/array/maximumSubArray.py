from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        maxSumUpToI = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > maxSum and maxSumUpToI < 0:
                maxSum = nums[i]
                maxSumUpToI = nums[i]
            else:
                if maxSumUpToI < 0:
                    maxSumUpToI = 0
                maxSumUpToI += nums[i]
                if maxSumUpToI > maxSum:
                    maxSum = maxSumUpToI

        return maxSum