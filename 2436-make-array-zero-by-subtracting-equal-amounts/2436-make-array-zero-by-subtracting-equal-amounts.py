class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        while sum(nums) > 0:
            curr_min = min(num for num in nums if num > 0)
            for i in range(n):
                if nums[i] > 0:
                    nums[i] -= curr_min
            ans += 1
        return ans
        