class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        a = [0] * n
        a[0] = 1 # n = 1
        a[1] = 2 # n = 2

        for i in range(2, n):
            a[i] = a[i - 1] + a[i - 2]

        return a[n - 1]
