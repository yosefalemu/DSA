class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False
        # Numbers ending with 0 (except 0 itself) are not palindromes
        if x > 0 and x % 10 == 0:
            return False
        
        reversed_num = 0
        original = x
        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
        
        return original == reversed_num