class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        duplicate_container = {}
        for i in range(len(nums)):
            if nums[i] in duplicate_container and abs(duplicate_container[nums[i]] - i) <= k:
                return True
            duplicate_container[nums[i]] = i
        return False 

        