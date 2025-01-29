class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        return self.fibImp(n,memo)
    def fibImp(self,n,memo) -> int:
        if n in memo:
            return memo[n]
        if n == 0:
            return 0
        if n == 1:
            return 1
        left = self.fibImp(n - 1,memo)
        right = self.fibImp(n - 2,memo)
        memo[n] = left + right
        return memo[n]

    



        