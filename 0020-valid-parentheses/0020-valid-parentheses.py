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
                if tempDic[c] != ans.pop():
                    return False
            else:
                ans.append(c)
        return not ans
        