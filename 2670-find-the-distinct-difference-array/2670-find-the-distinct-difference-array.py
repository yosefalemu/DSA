class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            left_sub = nums[:i + 1]
            right_sub = nums[i + 1:]
            ans.append(len(set(left_sub)) - len(set(right_sub)))
        return ans

        