# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        isbalance=True
        def checkbal(height,Node):
            nonlocal isbalance
            hl=height
            hr=height
            if Node and Node.left:
                hl=checkbal(height+1,Node.left)
            if Node and Node.right:
                hr=checkbal(height+1,Node.right)
            if abs(hl-hr)>1:
                isbalance=False
            return max(hl,hr)
            
        checkbal(1,root)
        return isbalance
            
                    