class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums1) - 1, -1, -1):
            # If nums2 is exhausted, just copy nums1
            if n == 0:
                break
            # If nums1 is exhausted or nums2's element is greater, copy from nums2
            if m == 0 or (n > 0 and nums2[n - 1] >= nums1[m - 1]):
                nums1[i] = nums2[n - 1]
                n -= 1
            else:
                nums1[i] = nums1[m - 1]
                m -= 1
