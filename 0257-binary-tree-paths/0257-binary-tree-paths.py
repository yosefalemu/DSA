# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def traverseTree(node,path):
            if not node:
                return
            if path:
                path += "->" + str(node.val)
            else:
                path = str(node.val)
            if not node.left and not node.right:
                ans.append(path)
                return
            traverseTree(node.left,path)
            traverseTree(node.right,path)
        traverseTree(root,"")
        return ans
        
        