class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def helper(number) -> int:
            if number in memo:
                return memo[number]
            if number == n:
                return 1
            if number > n:
                return 0
            memo[number] = helper(number + 1) + helper(number + 2)
            return memo[number]
        return helper(0)



        