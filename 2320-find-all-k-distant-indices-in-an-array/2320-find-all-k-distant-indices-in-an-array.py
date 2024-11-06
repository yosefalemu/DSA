class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ind_arr = []
        for ind,elem in enumerate(nums):
            if elem == key:
                ind_arr.append(ind)
        ans = []
        for i in range(len(nums)):
            for j in ind_arr:
                if abs(i - j) <= k:
                    ans.append(i)
                    break
        return ans
                    
