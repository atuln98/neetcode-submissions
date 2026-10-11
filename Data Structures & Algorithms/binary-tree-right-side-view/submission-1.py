# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result=[]
        q=[root]
        head=0
        while head<len(q):
            result.append(q[-1].val)
            for _ in range(len(q)-head):
                node=q[head]
                head+=1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return result
        