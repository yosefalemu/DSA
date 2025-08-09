class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        for right in range(len(nums)):
            if nums[left] != val:
                left += 1
                continue
            if nums[left] == val and nums[right] != val:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return left
        