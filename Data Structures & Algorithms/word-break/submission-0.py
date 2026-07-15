class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDictSet = set(wordDict)
        memo = {}
        def dfs(i, j):
            if j == len(s):
                return i == j
            state = (i, j)
            if state in memo:
                return memo[state]
            section = s[i:j + 1]
            skip = dfs(i, j + 1)
            break_word = False
            if section in wordDictSet:
                break_word = dfs(j + 1, j + 1)
            res = skip or break_word
            memo[state] = res
            return res
        return dfs(0, 0)