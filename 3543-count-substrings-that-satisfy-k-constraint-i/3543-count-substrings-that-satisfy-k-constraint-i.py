class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        ans = 0
        for i in range(len(s)):
            countZERO = 0
            countONE = 0
            for j in range(i,len(s)):
                if s[j] == "0":
                    countZERO += 1
                else:
                    countONE += 1
                if countZERO <= k or countONE <= k:
                    ans += 1
                else:
                    break
        return ans 

                


        