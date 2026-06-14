class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        currBoard = [['.' for _ in range(n)] for _ in range(n)]
        
        colsAttacked = set()
        diagAttacks = set()
        antiDiagAttacks = set()
        def dfs(i):
            if i == n:
                ans.append(["".join(row) for row in currBoard])
                return
            for j in range(n):
                if j not in colsAttacked and i + j not in diagAttacks and i - j not in antiDiagAttacks:
                    currBoard[i][j] = 'Q'
                    colsAttacked.add(j)
                    antiDiagAttacks.add(i - j)
                    diagAttacks.add(i + j)
                    dfs(i + 1)
                    currBoard[i][j] = '.'
                    colsAttacked.remove(j)
                    antiDiagAttacks.remove(i - j)
                    diagAttacks.remove(i + j)
        dfs(0)
        return ans
                

