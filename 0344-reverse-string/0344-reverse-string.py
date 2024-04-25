class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        leftPt = 0
        rightPt = len(s) - 1
        while leftPt < rightPt:
            s[leftPt],s[rightPt] = s[rightPt],s[leftPt]
            leftPt += 1
            rightPt -= 1
        
        