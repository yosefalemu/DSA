class Solution:
    def isValid(self, s: str) -> bool:
        tempDic = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        ans = []
        for c in s:
            if ans and c in tempDic:
                temp = ans.pop()
                if tempDic[c] != temp:
                    return False
            else:
                ans.append(c)
        return len(ans) == 0
        