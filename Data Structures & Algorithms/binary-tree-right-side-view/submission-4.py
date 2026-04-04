class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        ans = []
        while queue:
            level_size = len(queue)
            curr_nodes = []
            for _ in range(level_size):
                curr_node = queue.popleft()
                curr_nodes.append(curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            ans.append(curr_nodes[-1])
        return ans