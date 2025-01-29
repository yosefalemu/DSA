class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        first, second = 0, 1
        for _ in range(n - 2):
            first, second = second,first + second
        return first + second 

    



        