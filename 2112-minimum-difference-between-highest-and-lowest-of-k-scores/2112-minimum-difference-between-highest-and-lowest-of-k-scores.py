class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        numOfIteration = len(nums) - k + 1
        ans = inf
        for i in range(numOfIteration):
            temp = nums[i:i+k]
            ans = min(ans,temp[k - 1] - temp[0])
        return ans
            

        