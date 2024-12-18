# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        d = deque()
        d.append(cloned)
        while d:
            for i in range(len(d)):
                curr = d.popleft()
                if curr:
                    if curr.val == target.val:
                        return curr
                    if curr.left:
                        d.append(curr.left)
                    if curr.right:
                        d.append(curr.right)
        