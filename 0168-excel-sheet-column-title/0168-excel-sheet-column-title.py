class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber > 0:
            remainder = (columnNumber - 1) % 26
            ans = chr(65 + remainder) + ans
            columnNumber = (columnNumber - 1) // 26
        return ans
            
        