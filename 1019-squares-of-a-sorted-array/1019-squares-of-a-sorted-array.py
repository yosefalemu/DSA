class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        leftPt = 0
        rightPt = n - 1
        index = n - 1
        while leftPt <= rightPt:
            if abs(nums[leftPt]) >= abs(nums[rightPt]):
                ans[index] = nums[leftPt]**2
                leftPt += 1
            else:
                ans[index] = nums[rightPt]**2
                rightPt -= 1
            index -= 1
        return ans  

        