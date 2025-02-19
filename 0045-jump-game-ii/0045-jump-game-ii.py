class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        for i in range(len(nums)):
            currMaxJump = nums[i]
            j = 1
            while currMaxJump > 0:
                if i + j < len(dp) and dp[i + j] == 0:
                    dp[i + j] = dp[i] + 1
                j += 1
                currMaxJump -= 1
        return dp[-1]



        