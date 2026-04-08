class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count_zero = 0
        left_pt = 0
        zero_index = 0
        ans = 0
        for right_pt in range(len(nums)):
            if nums[right_pt] == 0:
                count_zero += 1
                if count_zero == 1:
                    zero_index = right_pt
            if count_zero > 1:
                left_pt = zero_index + 1
                zero_index = right_pt
                count_zero -= 1
            ans = max(ans, right_pt - left_pt + 1)
        return ans - 1
            

        