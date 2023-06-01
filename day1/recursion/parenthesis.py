from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        # pairs: parenthesis pairs we have to generate
        # unfinished: parenthesis that are not closed 
        def parenthesis(pairs: int, unfinished: int, path: str):
            if pairs == 0 and unfinished == 0:
                ans.append(path)
                return

            if pairs > 0: # we can open another pair
               parenthesis(pairs - 1, unfinished + 1, path + "(") 
            if unfinished > 0: # we can close a pair
                parenthesis(pairs, unfinished - 1, path + ")")

        parenthesis(n, 0, "")
        return ans
