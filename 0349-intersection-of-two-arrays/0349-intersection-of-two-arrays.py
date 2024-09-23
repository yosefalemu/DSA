class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1_dict = {}
        ans = set()
        for c in nums1:
            if c not in num1_dict:
                num1_dict[c] = 1
        for c in nums2:
            if c in num1_dict:
                ans.add(c)
        return ans
            