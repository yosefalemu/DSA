class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x > 0 and x % 10 == 0:
            return False
        reverse_num = 0
        original = x
        while x > 0:
            digit = x % 10
            reverse_num = (reverse_num*10) + digit
            x = x // 10
        return original == reverse_num