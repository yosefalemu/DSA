class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0]*(n + 1)
        dp[0] = 1
        for i in range(1,n + 1):
            #check for one
            if s[i - 1 : i] != "0":
                dp[i] += dp[i - 1]
            #check for two
            if i > 1 and 10 <= int(s[i - 2: i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]



        