class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        left = right = 0
        count = 1
        n = len(nums)
        while right < n:
            if nums[left] != nums[right]:
                count += 1
                left = right
            right += 1
        return count != n



        