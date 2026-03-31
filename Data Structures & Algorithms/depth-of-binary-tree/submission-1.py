# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # simple dfs might do the trick?        
        if not root:
            return 0
        
        def dfs(node, depth):
            
            if not node:
                return depth
            print("Node is: ", node.val, "\tdepth is: ", depth)
            return max(dfs(node.right, depth + 1), dfs(node.left, depth + 1))

        return dfs(root, 0)
