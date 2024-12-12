# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def traverseTree(node):
            if not node:
                return 0
            leftSum = 0
            if node.left and not node.left.left and not node.left.right:
                leftSum = node.left.val
            leftSum += traverseTree(node.left)
            leftSum += traverseTree(node.right)
            return leftSum
        return traverseTree(root)
            
        