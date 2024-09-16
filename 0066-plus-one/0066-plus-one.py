class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        added_number = [0]*len(digits)
        added_number[len(digits) - 1] = 1
        rightpt = len(digits) - 1
        carry = 0
        while rightpt >= 0:
            current_sum = digits[rightpt] + added_number[rightpt] + carry
            if current_sum == 10:
                digits[rightpt] = 0
                carry = 1
            else:
                digits[rightpt] = current_sum
                carry = 0
            rightpt -= 1
        if carry:
            ans = [1]
            for item in digits:
                ans.append(item)
            return ans
        return digits
        
        

        