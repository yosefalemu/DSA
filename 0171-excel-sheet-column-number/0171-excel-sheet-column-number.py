class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        lastIndex = len(columnTitle) - 1
        power = 0
        ans = 0
        while lastIndex >= 0:
            ans += (((ord(columnTitle[lastIndex]) + 1)%65)*pow(26,power))
            power += 1
            lastIndex -= 1
        return ans
            
        
        