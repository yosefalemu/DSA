class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        evenPointer = 0
        oddPointer = 1
        ans = [0]*len(nums)
        for num in nums:
            if num % 2 == 0:
                ans[evenPointer] = num
                evenPointer += 2
            else:
                ans[oddPointer] = num
                oddPointer += 2
        return ans
        