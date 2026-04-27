class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = 0
        multiplier = 1
        for i in range(len(digits) - 1, -1, -1):
            temp += multiplier*digits[i]
            multiplier *= 10
        return [int(num) for num in list(str(temp + 1))]



        