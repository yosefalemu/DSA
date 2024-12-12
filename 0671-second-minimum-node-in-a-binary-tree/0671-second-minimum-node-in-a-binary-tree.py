# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        nodesVal = []
        def traverseTree(node):
            if not node:
                return
            nodesVal.append(node.val)
            traverseTree(node.left)
            traverseTree(node.right)
        traverseTree(root)
        uniqueNodesVal = set(nodesVal)
        sortedVals = sorted(uniqueNodesVal)
        return sortedVals[1] if len(sortedVals) > 1 else -1        