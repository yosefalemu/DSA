class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total_sum = sum(nums)
        left_sum = 0
        ans = []
        for num in nums:
            right_sum = total_sum - num - left_sum
            ans.append(abs(left_sum - right_sum))
            left_sum += num
        return ans
        

        

        