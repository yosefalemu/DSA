class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        forward_arr = [0]*len(nums)
        reverse_arr = [0]*len(nums)
        forward_sum = 0 
        reverse_sum = 0
        for i in range(len(nums)):
            forward_sum += nums[i]
            forward_arr[i] = forward_sum
        for i in range(len(nums) - 1, -1, -1):
            reverse_sum += nums[i]
            reverse_arr[i] = reverse_sum
        for i in range(len(nums)):
            if forward_arr[i] == reverse_arr[i]:
                return i
        return -1



               


            

        