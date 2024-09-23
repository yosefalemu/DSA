class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        for c in nums:
            if c != 0:
                nums[index] = c
                index += 1
        for i in range(index,len(nums)):
            nums[i] = 0