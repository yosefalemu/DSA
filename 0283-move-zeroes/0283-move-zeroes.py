class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_pt = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero_pt] = nums[zero_pt], nums[i]
                zero_pt += 1

        

        

        