# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float('-inf')
        # some dfs approach for sure
        # if want to include a specific node we're at, we cut off the parent
        # if you only use one child (branch), it's still a valid path

        # base case:
        # if not a node
        # return 0
        # branch to the left or branch to the right (keep current sum)
        # include both branches (hard reset)
        # include one branch: max(curr node + dfs(left), curr node + dfs(right))
        # include both branches: curr node + dfs(left) + dfs(right)
        # max(one branch, both branches)?

        def dfs(curr):
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)
            cSum = curr.val + left + right
            self.ans = max(self.ans, cSum)
            return max(0, curr.val + max(left, right))
        dfs(root)
        return self.ans