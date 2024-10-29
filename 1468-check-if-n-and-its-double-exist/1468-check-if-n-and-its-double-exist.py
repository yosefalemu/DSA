class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        numDic = set()
        for c in arr:
            if c / 2 in numDic or c*2 in numDic:
                return True
            else:
                numDic.add(c)
        return False

        