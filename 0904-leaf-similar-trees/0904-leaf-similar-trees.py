# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafNodes1 = []
        leafNodes2 = []
        def traverseTree(node,leafNodes):
            if not node:
                return
            if not node.left and not node.right:
                leafNodes.append(node.val)
            traverseTree(node.left,leafNodes)
            traverseTree(node.right,leafNodes)
        # def traverseTree2(node):
        #     if not node:
        #         return
        #     if not node.left and not node.right:
        #         leafNodes2.append(node.val)
        #     traverseTree2(node.left)
        #     traverseTree2(node.right)
        traverseTree(root1,leafNodes1)
        traverseTree(root2,leafNodes2)
        return leafNodes1 == leafNodes2
        # length1 = len(leafNodes1)
        # length2 = len(leafNodes2)
        # if length1 != length2:
        #     return False
        # for i in range(length1):
        #     if leafNodes1[i] != leafNodes2[i]:
        #         return False
        # return True

        