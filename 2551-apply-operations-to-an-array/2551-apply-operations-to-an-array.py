class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        index = 0
        while index < len(nums) - 1:
            if nums[index] == nums[index + 1]:
                nums[index] *=2
                nums[index + 1] = 0
                index += 1
            index += 1
        ans = []
        count_zero = 0
        for c in nums:
            if c != 0:
                ans.append(c)
            else:
                count_zero += 1
        return ans + [0]*count_zero
        