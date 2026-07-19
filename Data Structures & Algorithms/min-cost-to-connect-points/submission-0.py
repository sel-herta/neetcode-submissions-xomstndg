class DSU:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = list(range(n))
    
    def find(self, n):
        if self.parent[n] == n:
            return n
        self.parent[n] = self.find(self.parent[n])
        return self.parent[n]
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if pu < pv:
            pu, pv = pv, pu
        self.rank[pu] ++ self.rank[pv]
        self.parent[pv] = pu
        return True
        

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dsu = DSU(n)
        edges = []
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                man_dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append((man_dist, i, j))
        edges.sort()
        res = 0
        for dist, u, v in edges:
            if dsu.union(u, v):
                res += dist
        return res