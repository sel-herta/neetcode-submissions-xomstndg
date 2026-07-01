class DSU:
    def __init__(self, n=0):
        self.parents = {}
        self.ranks = {}
        self.count = 0
        for i in range(n):
            self.add(i)

    def add(self, p):
        self.parents[p] = p
        self.ranks[p] = 1
        self.count += 1

    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv: 
            return False
        if self.ranks[pu] < self.ranks[pv]:
            self.parents[pu] = pv
        elif self.ranks[pu] > self.ranks[pv]:
            self.parents[pv] = pu
        else:        
            self.parents[pv] = pu
            self.ranks[pu] += 1
        self.count -= 1
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges = [(u, v, w, i) for i, (u, v, w) in enumerate(edges)]
        edges.sort(key=lambda x: x[2])

        def mstNoEdge(edgeIdx):
            dsu = DSU(n)
            ans = 0
            for i, (u, v, w, _) in enumerate(edges):
                # ont use
                if i == edgeIdx:
                    continue
                if dsu.union(u, v):
                    ans += w
            parent = dsu.find(0)
            ok = True
            for i in range(n):
                if dsu.find(i) != parent:
                    ok = False
                    break
            return ans if ok else float('inf')
        
        def mstEdge(edgeIdx):
            dsu = DSU(n)
            # use this edge first
            u0, v0, w0, _ = edges[edgeIdx]
            ans = w0
            dsu.union(u0, v0)
            for i, (u, v, w, _) in enumerate(edges):
                if i == edgeIdx:
                    continue
                if dsu.union(u, v):
                    ans += w
            parent = dsu.find(0)
            ok = True
            for i in range(n):
                if dsu.find(i) != parent:
                    ok = False
                    break
            return ans if ok else float('inf')
        
        base = mstNoEdge(-1)
        print(base)
        cri, pCri = set(), set()
        for i in range(len(edges)):
            wgtExcl = mstNoEdge(i)
            # MST total weight would increase
            if wgtExcl > base:
                cri.add(edges[i][3])
            else:
                wgtIncl = mstEdge(i)
                # MST total weight no change
                if wgtIncl == base:
                    pCri.add(edges[i][3])
    
        return [list(cri), list(pCri)]