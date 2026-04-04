class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(par, open, close):
            if open == n and close == n:
                res.append("".join(par))
                return
            if open < n:
                par.append("(")
                dfs(par, open + 1, close)
                par.pop()
            if close < open:
                par.append(")")
                dfs(par, open, close + 1)
                par.pop()
        
        dfs([], 0, 0)
        return res