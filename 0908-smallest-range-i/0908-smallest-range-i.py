class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        min_ele, max_ele = min(nums), max(nums)
        min_range, max_range = min_ele + k, max_ele - k
        if min_range >= max_range:
            return 0
        else:
            return max_range - min_range
        