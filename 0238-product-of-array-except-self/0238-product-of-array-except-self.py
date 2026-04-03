class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1]*n
        prefix_pro = 1
        for i in range(n):
            ans[i] = prefix_pro
            prefix_pro *= nums[i]
        suffix_pro = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= suffix_pro
            suffix_pro *= nums[i]
        return ans


            
        