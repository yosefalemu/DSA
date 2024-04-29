class Solution:
    def longestPalindrome(self, s: str) -> int:
        tempDic = {}
        for item in s:
            if item in tempDic:
                tempDic[item] += 1
            else:
                tempDic[item] = 1
        ans = 0
        oddValues = []
        for item in tempDic.values():
            if item % 2 == 0:
                ans += item
            else:
                ans += item - 1
                oddValues.append(item)
        if len(oddValues) > 0:
            return ans + 1
        else: return ans
        
            
            
            
        