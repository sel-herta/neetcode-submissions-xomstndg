class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            state = (i, j)
            if state in memo:
                return memo[state]
            res = 0
            skipi = dfs(i + 1, j)
            skipj = dfs(i, j + 1)
            match = 0
            if text1[i] == text2[j]:
                match = 1 + dfs(i + 1, j + 1)
            res = max(match, skipi, skipj)
            memo[state] = res
            return res
        return dfs(0, 0)