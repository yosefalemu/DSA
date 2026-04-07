class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        curr_count = 0
        for i in range(k):
            if s[i] in vowels:
                curr_count += 1
        max_count = curr_count
        for i in range(k, len(s)):
            curr_count += (s[i] in vowels) - (s[i - k] in vowels)
            max_count = max(max_count, curr_count)
        return max_count



        