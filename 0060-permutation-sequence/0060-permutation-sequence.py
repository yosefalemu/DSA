import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans = ""
        nums = [i for i in range(1,n+1)]
        for i in range(1,n+1):
            index = 0
            c = math.factorial(n-i)
            
            while c < k:
                index +=1
                k -= c
                
            ans += str(nums[index])
            del nums[index]
            
        return ans