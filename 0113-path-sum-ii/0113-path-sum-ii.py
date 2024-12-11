# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def traverseTree(node,path):
            if not node:
                return 
            if path:
                path.append(node.val)
            else:
                path = [node.val]
            if not node.left and not node.right:
                if sum(path) == targetSum:
                    ans.append(path.copy())
            traverseTree(node.left,path)
            traverseTree(node.right,path)
            path.pop()
        traverseTree(root,[])
        return ans
            

        