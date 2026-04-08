class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0
        left_pt = 0
        count_zero = 0
        for right_pt in range(len(nums)):
            if nums[right_pt] == 0:
                count_zero += 1
            while count_zero > k:
                if nums[left_pt] == 0:
                    count_zero -= 1
                left_pt += 1
            ans = max(ans, right_pt - left_pt + 1)
        return ans

        