# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        countItem = {}
        def traverseTree(node):
            if not node:
                return
            if node.val in countItem:
                countItem[node.val] += 1
            else:
                countItem[node.val] = 1
            traverseTree(node.left)
            traverseTree(node.right)
        traverseTree(root)
        maxItem = max(countItem.values())
        ans = []
        for key,value in countItem.items():
            if value == maxItem:
                ans.append(key)
        return ans
        