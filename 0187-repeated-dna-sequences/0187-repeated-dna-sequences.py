class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        n = len(s)
        tempDic = {}
        ans = set()
        for i in range(n):
            temp = s[i:i+10]
            if not temp in tempDic:
                tempDic[temp] = 1
                continue
            ans.add(temp)
        return list(ans)
            
            

        