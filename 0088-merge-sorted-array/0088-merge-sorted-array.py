class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index = m + n - 1
        m = m - 1
        n = n - 1
        while m >= 0 and n >= 0:
            if nums2[n] >= nums1[m]:
                nums1[index] = nums2[n]
                n -= 1
            else:
                nums1[index] = nums1[m]
                m -= 1
            index -= 1
        while n >= 0:
            nums1[index] = nums2[n]
            n -= 1
            index -= 1
        while m >= 0:
            nums1[index] = nums1[m]
            m -= 1
            index -= 1
