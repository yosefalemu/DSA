class Solution:
    def divisorGame(self, n: int) -> bool:
        turn = 0
        while n > 1:
            n -= 1
            turn += 1
        return not turn % 2 == 0
        
        