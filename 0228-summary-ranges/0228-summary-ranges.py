class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        start = 0
        ans = []
        for i in range(1,len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if start == i - 1:
                    ans.append(str(nums[start]))
                else:
                    ans.append(f"{nums[start]}->{nums[i - 1]}")
                start = i
        if start == len(nums) - 1:
            ans.append(str(nums[start]))
        else:
            ans.append(f"{nums[start]}->{nums[-1]}")   
        return ans
        
                    
                    
            
        