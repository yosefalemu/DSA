class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicated_container = {}
        for c in nums:
            if c in duplicated_container:
                return True
            else:
                duplicated_container[c] = 1
        return False
        