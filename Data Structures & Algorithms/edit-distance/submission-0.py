class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def dfs(i, j):
            if j == len(word2):
                return len(word1) - i
            if i == len(word1):
                return len(word2) - j
            state = (i, j)
            if state in memo:
                return memo[state]
            res = 0
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            insert = dfs(i + 1, j)
            delete = dfs(i, j + 1)
            replace = dfs(i + 1, j + 1)
            res = 1 + min(insert, delete, replace)
            memo[state] = res
            return res
        return dfs(0, 0)
            

            