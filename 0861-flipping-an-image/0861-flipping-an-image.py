class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        newRow = []
        for row in image:
            row.reverse()
            newCol = []
            for col in row:
                newCol.append(col ^ 1)
            newRow.append(newCol)
        return newRow


        