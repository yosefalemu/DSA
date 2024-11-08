class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ans = []
        leftPt, rightPt = 0, 0
        while leftPt < len(nums1) and rightPt < len(nums2):
            if nums1[leftPt][0] == nums2[rightPt][0]:
                ans.append([nums1[leftPt][0],(nums1[leftPt][1] + nums2[rightPt][1])])
                leftPt += 1
                rightPt += 1
            elif nums1[leftPt][0] < nums2[rightPt][0]:
                ans.append(nums1[leftPt])
                leftPt += 1
            else:
                ans.append(nums2[rightPt])
                rightPt += 1
        if leftPt < len(nums1):
            return ans + nums1[leftPt:]
        if rightPt < len(nums2):
            return ans + nums2[rightPt:]
        return ans

        