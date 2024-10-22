class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        leftPt, rightPt = 0, 0
        if name[0] != typed[0]:
            return False
        while rightPt < len(typed):
            if leftPt < len(name) and name[leftPt] == typed[rightPt]:
                leftPt += 1
                rightPt += 1
            elif leftPt > 0 and typed[rightPt] == name[leftPt - 1]:
                rightPt += 1
            else:
                return False
        return leftPt == len(name)
            
        