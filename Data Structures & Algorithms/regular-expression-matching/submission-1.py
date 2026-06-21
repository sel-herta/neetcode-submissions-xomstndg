class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dfs(i, j):
            if j == len(p):
                return i == len(s)
            state = (i, j)
            if state in memo:
                return memo[state]
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            if j + 1 < len(p) and p[j + 1] == '*':
                skip = dfs(i, j + 2)
                use = match and dfs(i + 1, j)
                memo[state] = skip or use
            else:
                memo[state] = match and dfs(i + 1, j + 1)
            return memo[state]
        return dfs(0, 0)
            
            