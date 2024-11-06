class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        leftPt = 0
        rightPt = len(nums) - 1
        ans = -1
        while leftPt < rightPt:
            if nums[leftPt] == -1 * nums[rightPt]:
                ans = abs(nums[rightPt])
                break
            else:
                if abs(nums[leftPt]) < abs(nums[rightPt]):
                    rightPt -= 1
                else:
                    leftPt += 1
        return ans
        