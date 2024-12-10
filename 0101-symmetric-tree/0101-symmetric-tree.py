# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSymmetricTraverse(left,right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            node1 = left
            node2 = right
            return isSymmetricTraverse(node1.left,node2.right) and isSymmetricTraverse(node1.right,node2.left)
        return isSymmetricTraverse(root.left,root.right)