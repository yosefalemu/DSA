class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans = 0
        leftpt = 0
        rightpt = 0
        while leftpt < len(g) and rightpt < len(s):
            if g[leftpt] <= s[rightpt]:
                ans += 1
                leftpt += 1
                rightpt += 1
            else:
                rightpt += 1    
        return ans
        