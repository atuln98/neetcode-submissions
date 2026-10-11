# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def checksame(p1,q1):
            if p1 is None and q1 is None:
                return True
            if p1 is None or q1 is None:
                return False
            if p1.val==q1.val:
                left = checksame(p1.left,q1.left)
                right = checksame(p1.right,q1.right)
                return left and right
            else:
                return False
        return checksame(p,q)
        