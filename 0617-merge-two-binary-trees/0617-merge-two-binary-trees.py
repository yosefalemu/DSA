# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverseTree(node1,node2):
            if not node1 and not node2:
                return
            node1Val = node1.val if node1 else 0
            node2Val = node2.val  if node2 else 0
            currSum = node1Val + node2Val
            currNode = TreeNode(currSum)
            currNode.left = traverseTree(node1.left if node1 and node1.left else None,node2.left if node2 and node2.left else None)
            currNode.right = traverseTree(node1.right if node1 and node1.right else None,node2.right if node2 and node2.right else None)
            return currNode
        return traverseTree(root1,root2)
        