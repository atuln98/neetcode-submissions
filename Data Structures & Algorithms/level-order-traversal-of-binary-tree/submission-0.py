# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result=[]
        def dfs(height,node):
            nonlocal result
            if node:
                if height == len(result):
                    result.append([])
                result[height].append(node.val)
                if node.left:
                    dfs(height+1,node.left)
                if node.right:
                    dfs(height+1,node.right)

        dfs(0,root)
        return result
        