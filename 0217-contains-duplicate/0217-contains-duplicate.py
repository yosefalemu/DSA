class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate = {}
        for num in nums:
            duplicate[num] = duplicate.get(num, 0) + 1
            if duplicate[num] > 1:
                return True
        return False
        