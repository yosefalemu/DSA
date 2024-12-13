# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafNodes1 = []
        leafNodes2 = []
        def traverseTree(node,leafNodes):
            if not node:
                return
            if not node.left and not node.right:
                leafNodes.append(node.val)
            traverseTree(node.left,leafNodes)
            traverseTree(node.right,leafNodes)
        traverseTree(root1,leafNodes1)
        traverseTree(root2,leafNodes2)
        return leafNodes1 == leafNodes2

        