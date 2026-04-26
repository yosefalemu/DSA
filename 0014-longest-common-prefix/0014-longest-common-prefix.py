class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        for i in range(1, len(strs)):
            leftpt, rightpt = 0, 0
            common = []
            while leftpt < len(ans) and rightpt < len(strs[i]):
                if ans[leftpt] == strs[i][rightpt]:
                    common.append(ans[leftpt])
                else:
                    break
                leftpt += 1
                rightpt += 1
            ans = "".join(common)
            if ans == "":
                return ""
        return ans



        