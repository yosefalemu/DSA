class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        leftPt,rightPt = 0,0
        while leftPt < len(nums1) and rightPt < len(nums2):
            if nums1[leftPt] == nums2[rightPt]:
                return nums1[leftPt]
            elif nums1[leftPt] < nums2[rightPt]:
                leftPt += 1
            else:
                rightPt += 1
        return -1
        