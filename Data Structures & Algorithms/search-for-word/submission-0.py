class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        # time: O(3^n)
        # space: O(n^2)

        currPath = set()
        def dfs(i, j, currWordIndex):
            # currWordIndex is the word we are looking for
            if currWordIndex == len(word):
                return True
            for dr, dc in dirs:
                nr, nc = i + dr, j + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if (nr, nc) not in currPath:
                        if board[nr][nc] == word[currWordIndex]:
                            currPath.add((nr, nc))
                            res = dfs(nr, nc, currWordIndex + 1)
                            if res:
                                return True
                            currPath.remove((nr, nc))
            
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    currPath.add((i, j))
                    if dfs(i, j, 1):
                        return True
                    currPath.remove((i, j))
        return False