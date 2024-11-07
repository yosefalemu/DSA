class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        ans = set()
        leftPt = 0
        rightPt = len(nums) - 1
        while leftPt < rightPt:
            num1 = nums[leftPt]
            num2 = nums[rightPt]
            average = (num1 + num2)/2
            ans.add(average)
            leftPt += 1
            rightPt -= 1
        return len(ans)
        