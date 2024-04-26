class Solution:
    def firstUniqChar(self, s: str) -> int:
        tempDic = {}
        for i in range(len(s)):
            if s[i] in tempDic:
                tempDic[s[i]].append(i)
            else:
                tempDic[s[i]] = [i]
        for item in tempDic:
            if len(tempDic[item]) == 1:
                return int(tempDic[item][0])
        return -1
        