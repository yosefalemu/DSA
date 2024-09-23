class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        leftpt, rightpt = 0, 0
        ans = []
        while leftpt < len(nums1) and rightpt < len(nums2):
            if nums1[leftpt] < nums2[rightpt]:
                leftpt += 1
            elif nums1[leftpt] > nums2[rightpt]:
                rightpt += 1
            else:
                ans.append(nums1[leftpt])
                leftpt += 1
                rightpt += 1
        return ans
                
        