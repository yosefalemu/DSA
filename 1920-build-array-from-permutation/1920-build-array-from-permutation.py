class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for num in nums:
            ans.append(nums[num])
        return ans

            
        