# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        depth = 0
        def traverseTree(node):
            nonlocal depth
            if not node:
                return
            depth += 1
            traverseTree(node.left)
            traverseTree(node.right)
        traverseTree(root)
        return depth

        