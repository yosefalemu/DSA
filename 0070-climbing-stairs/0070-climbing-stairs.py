class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        first, second = 1, 2
        for i in range(3,n + 1):
            first, second = second, first + second
        return second

        