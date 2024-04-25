class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dicS = {}
        dicT = {}
        for itemS,itemT in zip(s,t):
            if (itemS in dicS and dicS[itemS] != itemT) or (itemT in dicT and dicT[itemT] != itemS):
                return False
            else:
                dicS[itemS] = itemT
                dicT[itemT] = itemS
        return True
