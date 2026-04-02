class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        temp = list(s)
        leftpt = 0
        rightpt = len(s) - 1
        while leftpt < rightpt:
            while leftpt < rightpt and temp[leftpt] not in vowels:
                leftpt += 1
            while leftpt < rightpt and temp[rightpt] not in vowels:
                rightpt -= 1
            temp[leftpt], temp[rightpt] = temp[rightpt], temp[leftpt]
            leftpt += 1
            rightpt -= 1
        return "".join(temp)
            
        