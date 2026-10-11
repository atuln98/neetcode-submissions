# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        def dfs(height,node):
            nonlocal result
            if node:
                if len(result)<height:
                    result.append(node.val)
            if node and node.right:
                dfs(height+1,node.right)
            if node and node.left:
                dfs(height+1,node.left)

        dfs(1,root)
        return result



        