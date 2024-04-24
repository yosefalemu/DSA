class Solution:
    def isPalindrome(self, s: str) -> bool:
        tempStr = ""
        for eachItem in s:
            if ord(eachItem) in range(65, 91) or ord(eachItem) in range(97, 123) or ord(eachItem) in range(48, 58):
                tempStr += eachItem.lower()
        return tempStr == tempStr[::-1]
