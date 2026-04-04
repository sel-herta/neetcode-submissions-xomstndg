# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append([root, 1])

        d = defaultdict(list)

        while queue:
            node = queue.popleft()
            if node[0].left:
                queue.append([node[0].left, node[1] + 1])
            if node[0].right:
                queue.append([node[0].right, node[1] + 1])
            d[node[1]].append(node[0].val)
        
        ans = []
        for key, item in d.items():
            ans.append(item)
        return ans