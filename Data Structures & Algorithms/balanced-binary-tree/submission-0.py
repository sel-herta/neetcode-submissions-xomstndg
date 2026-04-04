# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dfs(node):
            if not node:
                return True, 0
            l_b, l_h = dfs(node.left)
            r_b, r_h = dfs(node.right)
            if not l_b or not r_b:
                return False, 0
            h = 1 + max(l_h, r_h)
            sub_diff = abs(l_h - r_h)
            if sub_diff <= 1:
                return True, h
            else:
                return False, h
        return dfs(root)[0]