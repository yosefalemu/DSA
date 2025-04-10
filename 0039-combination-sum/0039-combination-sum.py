class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(start, tempL):
            if sum(tempL) == target:
                ans.append(tempL[:])
                return
            if sum(tempL) > target:
                return
            for i in range(start,len(candidates)):
                tempL.append(candidates[i])
                helper(i,tempL)
                tempL.pop()    
        ans = []
        helper(0,[])
        return ans