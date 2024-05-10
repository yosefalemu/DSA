class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        start = 1
        while start <= n:
            if start % 3 == 0 and start % 5 == 0:
                ans.append("FizzBuzz")
            elif start % 3 == 0:
                ans.append("Fizz")
            elif start % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(start))
            start += 1
        return ans
        