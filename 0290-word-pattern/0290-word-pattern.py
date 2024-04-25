class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        dicP = {}
        dicS = {}
        for itemP,itemS in zip(pattern,s):
            if itemP in dicP and dicP[itemP] != itemS or itemS in dicS and dicS[itemS] != itemP:
                return False
            else:
                dicP[itemP] = itemS
                dicS[itemS] = itemP
        return True
        
        