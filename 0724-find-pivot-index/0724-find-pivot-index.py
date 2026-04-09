class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        prefix_sum = 0
        for i in range(len(nums)):
            right_sum = total_sum - nums[i] - prefix_sum
            if prefix_sum == right_sum:
                return i
            prefix_sum += nums[i]
        return -1




               


            

        