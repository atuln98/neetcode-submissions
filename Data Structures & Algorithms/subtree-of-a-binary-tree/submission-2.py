# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(a,b):
            if a is None and b is None:
                return True
            elif a is None or b is None:
                return False
            else:
                return a.val==b.val and same(a.left,b.left) and same(a.right,b.right)
        if root is None:
            return False
        if same(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        