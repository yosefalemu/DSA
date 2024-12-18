# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        ans = TreeNode()
        def traverseTree(node):
            nonlocal ans
            if not node:
                return
            if node.val == target.val:
                ans = node
            traverseTree(node.left)
            traverseTree(node.right)
        traverseTree(cloned)
        return ans
        