class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        seen = set()
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        minHeap = [[grid[0][0], 0, 0]]

        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if r == n - 1 and c == n - 1:
                return t
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    if (nr, nc) not in seen:
                        seen.add((nr, nc))
                        pushThis = [max(grid[nr][nc], t), nr, nc]
                        heapq.heappush(minHeap, pushThis)