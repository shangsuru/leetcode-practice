from typing import List

class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def subsetsRec(i, sub):
            ans.append(sub)
            for i in range(i, len(nums)):
                subsetsRec(i + 1, sub + [nums[i]])
        

        subsetsRec(0, [])
        return ans
        