class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        duplicate_container = {}
        for i in range(len(nums)):
            if nums[i] in duplicate_container and abs(i - duplicate_container[nums[i]]) <= k:
                return True
            else:
                duplicate_container[nums[i]] = i
        return False
        