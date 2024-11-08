class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        leftPt = 0
        rightPt = len(s) - 1
        listOfS = list(s)
        while leftPt < rightPt:
            if listOfS[leftPt] != listOfS[rightPt]:
                listOfS[leftPt] ,listOfS[rightPt] = min(s[leftPt],s[rightPt]), min(s[leftPt],s[rightPt])
            leftPt += 1
            rightPt -= 1
        return "".join(listOfS)

        