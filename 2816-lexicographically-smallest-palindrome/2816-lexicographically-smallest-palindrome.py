class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        leftPt = 0
        rightPt = len(s) - 1
        listOfS = list(s)
        while leftPt < rightPt:
            if listOfS[leftPt] != listOfS[rightPt]:
                min_char = min(s[leftPt],s[rightPt])
                listOfS[leftPt] ,listOfS[rightPt] = min_char, min_char 
            leftPt += 1
            rightPt -= 1
        return "".join(listOfS)

        