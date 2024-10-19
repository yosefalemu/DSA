class Solution:
    def reverseWords(self, s: str) -> str:
        listOfString = s.split()
        ans = ""
        for i in range(len(listOfString)):
            if i == len(listOfString) - 1:
                ans += listOfString[i][::-1]
            else:
                ans += listOfString[i][::-1] + " "
        return ans
        