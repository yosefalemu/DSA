from itertools import accumulate
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return list(accumulate(nums))