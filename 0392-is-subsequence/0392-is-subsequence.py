class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pt_s = pt_t = 0
        while pt_s < len(s) and pt_t < len(t):
            if t[pt_t] == s[pt_s]:
                pt_s += 1
            pt_t += 1
        return pt_s == len(s)
        