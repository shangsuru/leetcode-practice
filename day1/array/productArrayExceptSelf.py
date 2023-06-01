from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = []
        postfixes = []
        output = []

        # Compute prefixes
        product = 1
        for n in nums:
            product *= n
            prefixes.append(product)

        # ... and postfixes
        product = 1
        for n in nums[::-1]:
            product *= n
            postfixes.append(product)
        postfixes.reverse()

        # Compute final product as prefix * postfix
        output = []
        for i in range(len(nums)):
            val = 1
            if i - 1 >= 0:
                val *= prefixes[i - 1]
            if i + 1 < len(nums):
                val *= postfixes[i + 1]
            output.append(val)

        return output
            
