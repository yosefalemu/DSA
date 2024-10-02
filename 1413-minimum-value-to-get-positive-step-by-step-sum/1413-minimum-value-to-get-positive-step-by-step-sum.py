class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            nums[i] = curr_sum
        min_ele = min(nums)
        if min_ele < 0 :
            return -1*(min_ele - 1)
        else:
            return 1
        
        