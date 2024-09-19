class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev = [1]
        if rowIndex == 0:
            return prev
        for i in range(rowIndex):
            curr = [1]
            j = 1
            while j <= i:
                curr.append(prev[j - 1] + prev[j])
                j += 1
            curr.append(1)
            prev = curr
        return curr
            
        