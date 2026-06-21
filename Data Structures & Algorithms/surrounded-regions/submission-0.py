class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        surrounded = set()
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        def bfs(i, j):
            nonlocal surrounded
            if (i, j) in surrounded:
                return
            potential = set()
            q = deque()
            potential.add((i, j))
            q.append((i, j))
            validFill = True
            while q:
                ci, cj = q.popleft()
                # if on border, check if O and if it is, this is not a valid fill
                if ci == 0 or ci == rows - 1 or cj == 0 or cj == cols - 1:
                    if board[ci][cj] == 'O':
                        validFill = False
                        break
                for di, dj in dirs:
                    ni, nj = ci + di, cj + dj
                    if 0 <= ni < rows and 0 <= nj < cols:
                        if (ni, nj) not in potential:
                            if board[ni][nj] == 'O':
                                potential.add((ni, nj))
                                q.append((ni, nj))
            if validFill:
                surrounded = surrounded.union(potential)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and (i, j) not in surrounded:
                    bfs(i, j)
        for i in range(rows):
            for j in range(cols):
                if (i, j) in surrounded:
                    board[i][j] = 'X'