class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        evenPointer = 0
        oddPointer = 1
        n = len(nums)
        while evenPointer < n and oddPointer < n:
            if nums[oddPointer] % 2 != 0:
                oddPointer += 2
            elif nums[evenPointer] % 2 == 0:
                evenPointer += 2
            else:
                nums[oddPointer],nums[evenPointer] = nums[evenPointer],nums[oddPointer]
                evenPointer += 2
                oddPointer += 2
        return nums
        