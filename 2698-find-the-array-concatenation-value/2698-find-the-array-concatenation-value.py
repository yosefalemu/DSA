class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        leftPt = 0
        rightPt = len(nums) - 1
        ans = 0
        while leftPt < rightPt:
            concatString = str(nums[leftPt]) + str(nums[rightPt])
            ans += int(concatString)
            leftPt += 1
            rightPt -= 1
        if leftPt == rightPt:
            ans += nums[leftPt]
        return ans

        