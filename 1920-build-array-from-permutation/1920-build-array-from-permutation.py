class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        #Decode
        for i in range(n):
            nums[i] += n*(nums[nums[i]] % n)
        #Encode
        for i in range(n):
            nums[i] //= n
        return nums



        