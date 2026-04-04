# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recur(self, root, good_val):
        if not root:
            return 0
        plus = 1 if root.val >= good_val else 0
        new_val = max(good_val, root.val)
        left = self.recur(root.left, new_val)
        right = self.recur(root.right, new_val)
        return plus + left + right

    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.recur(root, root.val)