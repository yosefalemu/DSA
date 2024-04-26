class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dicS = {}
        dicT = {}
        for item in s:
            if item in dicS:
                dicS[item] += 1
            else:
                dicS[item] = 1
        for item in t:
            if item in dicT:
                dicT[item] += 1
            else:
                dicT[item] = 1
        for item in dicT:
            if item not in dicS.keys():
                return item
            else:
                if dicT[item] != dicS[item]:
                    return item
                
        