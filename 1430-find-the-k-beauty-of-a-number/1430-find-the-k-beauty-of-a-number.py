class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        ans = 0
        strNum = str(num)
        numOfIteration = len(strNum) - k + 1
        for i in range(numOfIteration):
            temp = strNum[i:i+k]
            tempInt = int(temp)
            if tempInt != 0 and num % tempInt == 0:
                ans += 1
        return ans
        