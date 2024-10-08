class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count_zero = 0
        all_prod = 1
        for c in nums:
            if c == 0:
                count_zero += 1
            else:
                all_prod *= c
        more_zero = count_zero > 1
        zero_found = count_zero == 1
        if more_zero:
            return [0]*len(nums)
        for i in range(len(nums)):
            if zero_found:
                if nums[i] != 0:
                    nums[i] = 0
                else:
                    nums[i] = all_prod
            else:
                nums[i] = all_prod // nums[i]
        return nums
                
            
        