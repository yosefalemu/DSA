class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = [0]*len(nums)
        ans[0] = nums[0]
        for i in range(1,len(nums)):
            if nums[i] >= 0:
                if ans[i - 1] >= 0:
                    ans[i] = ans[i - 1] + nums[i]
                else:
                    ans[i] = nums[i]
            else:
                if ans[i - 1] >= 0:
                    ans[i] = ans[i - 1] + nums[i]
                else:
                    ans[i] = nums[i]
        return max(ans)

        