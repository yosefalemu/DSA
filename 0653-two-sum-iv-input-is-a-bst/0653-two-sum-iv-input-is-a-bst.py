# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        allVal = []
        def traverseTree(node):
            if not node:
                return
            allVal.append(node.val)
            traverseTree(node.left)
            traverseTree(node.right)
        traverseTree(root)
        allVal.sort()
        leftPt = 0
        rightPt = len(allVal) - 1
        while leftPt < rightPt:
            currSum = allVal[leftPt] + allVal[rightPt]
            if currSum == k:
                return True
            elif currSum > k:
                rightPt -= 1
            else:
                leftPt += 1
        return False
        