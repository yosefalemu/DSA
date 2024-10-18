class Solution:
    def isHappy(self, n: int) -> bool:
        # visit_set = set()
        # while n not in visit_set:
        #     visit_set.add(n)
        #     n = self.findSquareOfEach(n)
        #     if n == 1:
        #         return True
        # return False
        slow = n
        fast = self.findSquareOfEach(n)
        while fast != 1 and slow != fast:
            slow = self.findSquareOfEach(slow)
            fast = self.findSquareOfEach(self.findSquareOfEach(fast))
        return fast == 1
    def findSquareOfEach(self,n:int)->int:
        current_sum = 0
        while n:
            digit = n % 10
            current_sum += digit**2
            n //= 10
        return current_sum

        