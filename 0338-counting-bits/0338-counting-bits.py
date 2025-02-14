class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)
        currPowerTwo = 1
        for i in range(1, n + 1):
            if i == currPowerTwo*2:
                currPowerTwo = currPowerTwo*2
            ans[i] = 1 + ans[i - currPowerTwo]
        return ans