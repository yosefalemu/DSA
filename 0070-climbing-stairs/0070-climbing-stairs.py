class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def helper(curr):
            if curr in memo:
                return memo[curr]
            if curr == 1:
                return 1
            if curr == 2:
                return 2
            memo[curr] = helper(curr - 1) + helper(curr - 2)
            return memo[curr]
        return helper(n)
            




        