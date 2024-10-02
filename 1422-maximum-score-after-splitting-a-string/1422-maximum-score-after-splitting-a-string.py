class Solution:
    def maxScore(self, s: str) -> int:
        num_zero = 0
        num_one = s.count("1")
        ans = 0
        for i in range(len(s) - 1):
            if s[i] == "0":
                num_zero += 1
            else:
                num_one -= 1
            ans = max(ans,num_zero + num_one)
        return ans
        
        