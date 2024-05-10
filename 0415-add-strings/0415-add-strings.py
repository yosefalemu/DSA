class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = ""
        carry = 0
        ptr1, ptr2 = len(num1) - 1, len(num2) - 1
        
        while ptr1 >= 0 or ptr2 >= 0 or carry:
            digit_sum = carry
            if ptr1 >= 0:
                digit_sum += int(num1[ptr1])
                ptr1 -= 1
            if ptr2 >= 0:
                digit_sum += int(num2[ptr2])
                ptr2 -= 1
            
            carry, digit = divmod(digit_sum, 10)
            ans = str(digit) + ans
        
        return ans