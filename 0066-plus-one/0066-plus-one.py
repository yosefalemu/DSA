class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pointer = len(digits) - 1
        while pointer >= 0:
            if digits[pointer] == 9:
                digits[pointer] = 0
            else:
                digits[pointer] += 1
                return digits
            pointer -= 1
        return [1] + digits
        
        

        