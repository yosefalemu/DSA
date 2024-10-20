class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        countList = []
        count = 0
        curr = s[0]
        for  c in s:
            if c != curr:
                countList.append(count)
                curr = c
                count = 1
            else:
                count += 1
        countList.append(count)
        ans = 0
        first = 0 
        second = 1
        while second < len(countList):
            ans += min(countList[first],countList[second])
            first += 1
            second += 1
        return ans
