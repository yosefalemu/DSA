# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        def traverseTree(node):
            nonlocal ans
            if not node:
                return
            if node.val >= low and node.val <= high:
                ans += node.val
                traverseTree(node.left)
                traverseTree(node.right)
            elif node.val < low:
                traverseTree(node.right)
            elif node.val > high:
                traverseTree(node.left)
        traverseTree(root)
        return ans

        