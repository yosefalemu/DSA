class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev = [1]
        for i in range(rowIndex):
            temp = [1]
            if len(prev) >= 2:
                left = 0
                right = 1
                while right < len(prev):
                    temp.append(prev[left] + prev[right])
                    left += 1
                    right += 1
            temp.append(1)
            prev = temp
        return prev
        