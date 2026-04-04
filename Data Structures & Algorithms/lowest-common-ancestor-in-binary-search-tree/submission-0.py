class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        
        curr_val = root.val
        p_val = p.val
        q_val = q.val

        if p_val < curr_val and q_val < curr_val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p_val > curr_val and q_val > curr_val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root