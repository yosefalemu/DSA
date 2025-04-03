class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        def findMaxRob(arrNum):
            dp = [0]*(n - 1)
            dp[0] = arrNum[0]
            dp[1] = max(arrNum[0],arrNum[1])
            for i in range(2, n - 1):
                dp[i] = max(dp[i - 2] + arrNum[i], dp[i - 1])
            return dp[-1]
        return max(findMaxRob(nums),findMaxRob(nums[::-1]))