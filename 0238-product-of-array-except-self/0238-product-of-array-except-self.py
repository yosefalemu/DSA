class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        count_zero = 0
        for num in nums:
            if num == 0:
                count_zero += 1
                continue
            product *= num
        if count_zero > 1:
            return [0]*len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = product
            elif count_zero == 1 and nums[i] != 0:
                nums[i] = 0
            else:
                nums[i] = product // nums[i]
        return nums


            
        