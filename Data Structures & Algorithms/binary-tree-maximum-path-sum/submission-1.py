class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = float('-inf')

        def down(node):
            nonlocal best
            if not node:
                return 0

            left = down(node.left)      # best path going down the left side
            right = down(node.right)    # best path going down the right side

            # Job 1: best path that bends at this node (node is the top of the path)
            best = max(best,
                       node.val,                    # just the node
                       node.val + left,             # node and left branch
                       node.val + right,            # node and right branch
                       node.val + left + right)     # node and both branches

            # Job 2: best path going down from this node, for the parent to use
            return max(node.val,                    # stop here
                       node.val + left,             # continue left
                       node.val + right)            # continue right

        down(root)
        return best