class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left, right = 0, 0
        charDic = {}
        ans = -inf
        while right < len(s):
            rightChar = s[right]
            charDic[rightChar] = charDic.get(rightChar,0) + 1
            while charDic[rightChar] > 2:
                leftChar = s[left]
                charDic[leftChar] -= 1
                if charDic[leftChar] == 0:
                    del charDic[leftChar]
                left += 1
            ans = max(ans,right - left + 1)
            right += 1
        return ans
                
            


        