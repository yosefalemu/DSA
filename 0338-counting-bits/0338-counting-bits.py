class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0,1]
        ans = [0]*(n+1)
        ans[1] = ans[2] = 1
        currPowerTwo = 2
        for i in range(2,len(ans)):
            if math.log2(i).is_integer():
                currPowerTwo = i
                ans[i] = 1
            else:
                ans[i] = ans[currPowerTwo] + ans[i - currPowerTwo]
        return ans