# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        ans = []
        def traverseTree(node,pathSum):
            if not node:
                return
            if pathSum:
                pathSum += node.val
            else:
                pathSum = node.val
            if not node.left and not node.right:
                ans.append(pathSum)
                return
            traverseTree(node.left,pathSum)
            traverseTree(node.right,pathSum)
        traverseTree(root,0)
        return targetSum in ans
        