class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        def bfs(i, j, ocean):
            if (i, j) in ocean:
                return
            q = deque()
            q.append((i, j))
            ocean.add((i, j))
            while q:
                ci, cj = q.popleft()
                for di, dj in dirs:
                    ni, nj = ci + di, cj + dj
                    if 0 <= ni < rows and 0 <= nj < cols:
                        if (ni, nj) not in ocean:
                            if heights[ni][nj] >= heights[ci][cj]:
                                ocean.add((ni, nj))
                                q.append((ni, nj))
        # bfs from borders: pacific and atlantic
        for i in range(rows):
            bfs(i, 0, pacific)
            bfs(i, cols - 1, atlantic)
        for j in range(cols):
            bfs(0, j, pacific)
            bfs(rows - 1, j, atlantic)
        return list(pacific.intersection(atlantic))