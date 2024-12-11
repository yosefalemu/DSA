# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftLevel = 1
        rightLevel = 1
        leftNode, rightNode = root.left, root.right
        while leftNode:
            leftNode = leftNode.left
            leftLevel += 1
        while rightNode:
            rightNode = rightNode.right
            rightLevel += 1
        if leftLevel == rightLevel:
            return (2**leftLevel) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        

        