# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0
        depth = 0
        nodeDic = {}
        def traverseNode(node):
            nonlocal ans,depth
            if not node:
                ans = max(ans, depth)
                return
            if node in nodeDic:
                depth = nodeDic[depth]
            else:
                depth += 1
                nodeDic[node] = depth
            traverseNode(node.left)
            traverseNode(node.right)
            depth -= 1
        traverseNode(root)
        return ans

        