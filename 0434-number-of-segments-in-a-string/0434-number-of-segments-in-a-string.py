class Solution:
    def countSegments(self, s: str) -> int:
        temp = ""
        ans  = 0
        for item in s:
            if item != " ":
                temp += item
            else:
                if temp:
                    ans += 1
                    temp =""
        if temp:
            return ans + 1
        else:
            return ans
                
            
                
        