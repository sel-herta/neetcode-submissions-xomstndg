class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r_hash = collections.defaultdict(set)
        c_hash = collections.defaultdict(set)
        s_hash = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in r_hash[r] or board[r][c] in c_hash[c] or board[r][c] in s_hash[(r // 3, c // 3)]:
                    return False
                r_hash[r].add(board[r][c])
                c_hash[c].add(board[r][c])
                s_hash[(r // 3, c // 3)].add(board[r][c])
        return True

        
                
        
