class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        index = 0
        dp1 = [0]*(n - 1)
        if index == 0:
            dp1[0] = nums[0]
            dp1[1] = max(nums[0],nums[1])
            for i in range(2, n - 1):
                dp1[i] = max(dp1[i - 2] + nums[i], dp1[i - 1])
        dp2 = [0]*(n - 1)
        nums.reverse()
        if index == 0:
            dp2[0] = nums[0]
            dp2[1] = max(nums[0],nums[1])
            for i in range(2, n - 1):
                dp2[i] = max(dp2[i - 2] + nums[i], dp2[i - 1])
        return max(dp1[-1], dp2[-1])
        

        