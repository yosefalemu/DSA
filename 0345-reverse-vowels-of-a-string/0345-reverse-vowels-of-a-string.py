class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        temp = []
        for char in s:
            if char in vowels:
                temp.append(char)
        temp_index = len(temp) - 1
        ans = ""
        for i in range(len(s)):
            if s[i] in vowels:
                ans += temp[temp_index]
                temp_index -= 1
            else:
                ans += s[i]
        return ans
        