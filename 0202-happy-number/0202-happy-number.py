class Solution:
    def isHappy(self, n: int) -> bool:
        visit_set = set()
        while n not in visit_set:
            visit_set.add(n)
            n = self.findSquareOfEach(n)
            if n == 1:
                return True
        return False
    def findSquareOfEach(self,n:int)->int:
        current_sum = 0
        while n != 0:
            current_sum += (n % 10)**2
            n //= 10
        return current_sum

        