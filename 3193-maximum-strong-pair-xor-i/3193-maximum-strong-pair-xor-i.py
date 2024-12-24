class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        ans = -inf
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                num1,num2 = nums[i],nums[j]
                if num2 - num1 <= num1:
                    ans = max(ans,num1^num2)
        return ans

        