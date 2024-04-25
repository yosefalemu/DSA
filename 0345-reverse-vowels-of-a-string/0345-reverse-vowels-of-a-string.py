class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s = list(s)
        leftPt = 0
        rightPt = len(s) - 1
        while leftPt < rightPt:
            if s[leftPt] in vowels and s[rightPt] in vowels:
                s[leftPt],s[rightPt] = s[rightPt],s[leftPt]
                leftPt += 1
                rightPt -= 1
            elif s[leftPt] in vowels and s[rightPt] not in vowels:
                rightPt -= 1
            elif s[leftPt] not in vowels and s[rightPt] in vowels:
                leftPt += 1
            else:
                leftPt += 1
                rightPt -= 1
        return "".join(s)
        
        