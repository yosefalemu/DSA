class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def helper(openP,closeP,s):
            if openP == closeP and openP + closeP == n*2:
                ans.append(s)
                return
            if openP < n:
                helper(openP + 1,closeP, s + "(")
            if closeP < openP:
                helper(openP,closeP + 1, s + ")")
            return
        helper(0,0,"")
        return ans
        