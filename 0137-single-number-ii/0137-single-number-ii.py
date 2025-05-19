class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dicNum = {}
        for c in nums:
            if c in dicNum:
                dicNum[c] += 1
            else:
                dicNum[c] = 1
        for key, value in dicNum.items():
            if value == 1:
                return key
        