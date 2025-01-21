class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        current = 0
        total = 0
        for i in range(2,n):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                current += 1
                total += current
            else:
                current = 0
        return total

        