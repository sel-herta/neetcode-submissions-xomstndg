# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(cp, cq):
            if not cp and not cq:
                return True
            if (not cp and cq) or (not cq and cp):
                return False
            if cp.val != cq.val:
                return False
            left = dfs(cp.left, cq.left)
            right = dfs(cp.right, cq.right)
            return left and right
        return dfs(p, q)