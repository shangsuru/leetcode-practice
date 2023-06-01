class Solution:
    def sortString(self, s: str) -> str:
        return ''.join(sorted(s))
    
    def isAnagram(self, s: str, t: str) -> bool:
        return self.sortString(s) == self.sortString(t)
        