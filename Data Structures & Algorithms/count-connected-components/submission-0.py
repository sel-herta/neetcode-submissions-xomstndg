class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        visited = set()
        def dfs(node):
            nonlocal visited
            if node in visited:
                return
            visited.add(node)
            stack = [node]
            while stack:
                u = stack.pop()
                for v in adjList[u]:
                    if v not in visited:
                        visited.add(v)
                        stack.append(v)
        
        ans = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                ans += 1
        return ans