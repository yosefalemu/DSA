class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLength = float('inf')
        for s in strs:
            minLength = min(minLength,len(s))
        ans = ""
        while minLength >= 0:
            ans = strs[0][:minLength]
            flag = True
            for s in strs:
                if s[:minLength] != ans:
                    flag = False
                    break
            if flag:
                return ans
            else:
                minLength -= 1
        return ans
            
        