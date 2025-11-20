class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = lambda nums: list(accumulate(nums))
        return ans(nums)