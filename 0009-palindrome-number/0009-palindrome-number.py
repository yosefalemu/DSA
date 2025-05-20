class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = str(x)
        left = 0
        right = len(temp) - 1
        while left < right:
            if temp[left] != temp[right]:
                return False
            left += 1
            right -= 1
        return True
        