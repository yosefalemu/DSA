class Solution:
    def minPatches(self, nums: List[int], ssum: int) -> int:
        n=len(nums)
        limit,cnt=0,0
        for i in range(n):
            if nums[i]>limit+1:
                while nums[i]>limit+1:
                    limit+=limit+1
                    cnt+=1
                    if limit>=ssum: break
            limit+=nums[i]
            if limit>=ssum: break
        while limit<ssum:
            limit+=limit+1
            cnt+=1
        return cnt