# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root: TreeNode, m: list[int]) -> int:
    res = 0
    if root:
        left = maxPathSum(root.left, m)
        right = maxPathSum(root.right, m)
        res = max(left+root.val, right+root.val, root.val)
        m[0] = max(m[0], left+right+root.val, res)
    return res

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        m = [-1001]
        maxPathSum(root, m)
        return m[0]