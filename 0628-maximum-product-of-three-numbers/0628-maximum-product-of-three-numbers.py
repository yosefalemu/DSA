class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        posetive = []
        negative = []
        if len(nums) == 3:
            return nums[0]*nums[1]*nums[2]
        for c in nums:
            if c >= 0:
                posetive.append(c)
            else:
                negative.append(c)
        posetive.sort()
        negative.sort()
        if len(negative) <= 1:
            return posetive[-1]*posetive[-2]*posetive[-3]
        else:
            if len(posetive) == 0:
                return negative[-1]*negative[-2]*negative[-3]
            elif len(posetive) == 1:
                return negative[0]*negative[1]*posetive[-1]
            elif len(posetive) == 2:
                return negative[0]*negative[1]*posetive[-1]
            else:
                return max(negative[0]*negative[1]*posetive[-1],posetive[-1]*posetive[-2]*posetive[-3])
                
        
        