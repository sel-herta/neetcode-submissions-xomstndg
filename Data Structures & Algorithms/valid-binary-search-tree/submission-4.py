# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, currMin, currMax):
        if not root:
            return True
        if not (currMin < root.val < currMax):
            return False
        return self.dfs(root.left, currMin, root.val) and self.dfs(root.right, root.val, currMax)
        

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, float('-inf'), float('inf'))