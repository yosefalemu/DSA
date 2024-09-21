class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        leftpt,rightpt = 0,len(nums) - 1
        while leftpt < rightpt:
            mid = (leftpt + rightpt) // 2
            if nums[mid] > nums[mid + 1]:
                rightpt = mid
            else:
                leftpt = mid + 1
        return leftpt
        