"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        adjList = defaultdict(list)
        q = deque()
        q.append(node)
        visited = set()
        visited.add(node)

        nodeCopies = defaultdict(Node)
        nodeCopies[node.val] = Node(node.val)

        while q:
            u = q.popleft()
            for v in u.neighbors:
                if v.val not in nodeCopies:
                    q.append(v)
                    nodeCopies[v.val] = Node(v.val)
                nodeCopies[u.val].neighbors.append(nodeCopies[v.val])
                #nodeCopies[v.val].neighbors.append(nodeCopies[u.val])
        return nodeCopies[node.val]
        
            