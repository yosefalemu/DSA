class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freqChar = {}
        ans = 0
        maxFreqChar = 0
        for right in range(len(s)):
            freqChar.setdefault(s[right],0)
            freqChar[s[right]] += 1
            maxFreqChar = max(maxFreqChar,freqChar[s[right]])
            if (right - left + 1) - maxFreqChar > k:
                freqChar[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans

        

