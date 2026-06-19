class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        visited = set()
        def dfs(u, par):
            if u in visited:
                return False
            visited.add(u)
            for v in adjList[u]:
                if v == par:
                    continue
                if not dfs(v, u):
                    return False
            return True
        return dfs(0, -1) and len(visited) == n
        