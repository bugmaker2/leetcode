class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        step = [None]*n
        step[0] = 1
        step[1] = 2
        for i in range(2,n):
            step[i] = step[i-1] + step[i-2]
        return step[n-1]
