# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def traverseTree(node,depth):
            if not node:
                return depth
            return  max(traverseTree(node.left,depth + 1),traverseTree(node.right,depth + 1))
        return traverseTree(root,0)

            

        