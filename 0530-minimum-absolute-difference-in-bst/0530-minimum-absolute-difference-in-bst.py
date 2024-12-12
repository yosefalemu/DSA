# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        nodeValues = []
        def traverseTree(node):
            if not node:
                return
            nodeValues.append(node.val)
            traverseTree(node.left)
            traverseTree(node.right)
        traverseTree(root)
        nodeValues.sort()
        ans = float("inf")
        for i in range(1,len(nodeValues)):
            ans = min(ans,nodeValues[i] - nodeValues[i - 1])
            if ans == 1:
                break
        return ans
        