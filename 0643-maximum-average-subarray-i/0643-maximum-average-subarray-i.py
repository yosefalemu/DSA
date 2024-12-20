class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        numOfIteration = len(nums) - k + 1
        currSum = sum(nums[:k])
        ans = currSum/k
        for i in range(1,numOfIteration):
            currSum = currSum - nums[i - 1] + nums[i + k - 1]
            ans = max(ans,currSum/k)
        return ans

            
            
            
        