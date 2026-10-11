# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        good_nodes=0
        def dfs(maxinroute,node):
            nonlocal good_nodes
            if node.val>=maxinroute:
                good_nodes+=1
                maxinroute=node.val
            if node.left:
                dfs(maxinroute,node.left)
            if node.right:
                dfs(maxinroute,node.right)

        dfs(root.val,root)
        return good_nodes
        