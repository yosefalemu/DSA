class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        temp = ""
        for char in s:
            if char.isdigit():
                temp += char
            elif char.isalpha():
                temp += char.upper()
            else:
                pass
        controller = 0
        i = len(temp) - 1
        ans = ""
        while i >= 0:
            if controller < k:
                ans = temp[i] + ans
                i -= 1
                controller += 1
            else:
                ans = "-" + ans
                controller = 0
        return ans
            

        
        