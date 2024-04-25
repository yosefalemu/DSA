class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicS = {}
        dicT = {}
        for itemS in s:
            if itemS in dicS:
                dicS[itemS] += 1
            else:
                dicS[itemS] = 1
        for itemT in t:
            if itemT in dicT:
                dicT[itemT] += 1
            else:
                dicT[itemT] = 1
        if set(dicS.keys()) != set(dicT.keys()):
            return False
        for keyOfS in dicS.keys():
            if dicS[keyOfS] != dicT[keyOfS]:
                return False
        return True
                
        