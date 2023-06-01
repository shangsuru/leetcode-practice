from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def combineRec(num: int, remainingLength: int, path: List[int]):
            if remainingLength == 0: # valid combination found
                ans.append(path)
                return

            if num > n: # num out of range
                return

            # choose num for the path
            combineRec(num + 1, remainingLength - 1, path + [num])
            # ...or don't include it in the path
            combineRec(num + 1, remainingLength, path)
            

        combineRec(1, k, [])

        return ans