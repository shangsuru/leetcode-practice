class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {str(s[0]): 0}
        length = 1
        maxLength = 1
        start = 0

        for i, c in enumerate(s):
            if c in seen:
                start = seen[c] + 1
                seen[c] = i
                length = max(0, length - 1)
            else:
                length += 1
                if length > maxLength:
                    maxLength = length
                seen[c] = i

        return maxLength