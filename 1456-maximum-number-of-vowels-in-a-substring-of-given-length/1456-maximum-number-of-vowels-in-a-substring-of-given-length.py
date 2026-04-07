class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        curr_count = 0
        for i in range(k):
            if s[i] in vowels:
                curr_count += 1
        max_count = curr_count
        for i in range(k, len(s)):
            vowel_inc = s[i] in vowels
            vowel_dec = s[i - k] in vowels
            curr_count += (1 if vowel_inc else 0) + (-1 if vowel_dec else 0)
            max_count = max(max_count, curr_count)
        return max_count



        