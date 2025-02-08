class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        left = 1
        right = 2
        for stairCase in range(3,n + 1):
            ans = left + right
            left, right = right, left + right
        return ans


        