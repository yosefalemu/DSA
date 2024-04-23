class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ""
        rem = ""
        lenOfA = len(a)
        lenOfB = len(b)
        if lenOfA > lenOfB:
            b = "0"*(lenOfA - lenOfB) + b
        if lenOfB > lenOfA:
            a = "0"*(lenOfB - lenOfA) + a
        lenOfA = len(a) - 1
        lenOfB = len(b) - 1
        while lenOfA >= 0 and lenOfB >= 0:
            if rem:
                if a[lenOfA] == "1" and b[lenOfB] == "1":
                    ans += "1"
                elif a[lenOfA] == "0" and b[lenOfB] == "0":
                    ans += "1"
                    rem = ""
                else:
                    ans += "0"
            else:
                if a[lenOfA] == "1" and b[lenOfB] == "1":
                    ans += "0"
                    rem = "1"
                elif a[lenOfA] == "0" and b[lenOfB] == "0":
                    ans += "0"
                else:
                    ans += "1"
            lenOfA -= 1
            lenOfB -= 1
        if rem:
            ans += "1"
        return ans[::-1]
            
                
        