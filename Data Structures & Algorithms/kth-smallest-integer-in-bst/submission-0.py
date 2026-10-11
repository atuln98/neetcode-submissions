# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        visitedvals=[]
        def dfs(node):
            nonlocal visitedvals
            nonlocal k
            if len(visitedvals) == k:
                return
            if node.left:
                dfs(node.left)
            visitedvals.append(node.val)
            if node.right:
                dfs(node.right)
        dfs(root)
        return visitedvals[k-1]

        