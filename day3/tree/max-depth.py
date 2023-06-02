from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def maxDepthRec(node: TreeNode, depth: int):
            if not node:
                return depth
                
            return max(
                maxDepthRec(node.left, depth + 1),
                maxDepthRec(node.right, depth + 1)
            )

        return maxDepthRec(root, 0)