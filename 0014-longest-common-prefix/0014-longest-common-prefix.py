class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        for i in range(1, len(strs)):
            leftpt, rightpt = 0, 0
            common = ""
            while leftpt < len(ans) and rightpt < len(strs[i]):
                if ans[leftpt] == strs[i][rightpt]:
                    common += ans[leftpt]
                else:
                    if len(common) == 0:
                        return ""
                    else:
                        ans = common
                        break
                leftpt += 1
                rightpt += 1
        return ans



        