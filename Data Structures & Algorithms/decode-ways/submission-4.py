class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            ways = 0
            ways += dfs(i + 1)
            if i + 1 < len(s):
                one = s[i] == "1"
                two = s[i] == "2"
                if one:
                    ways += dfs(i + 2)
                elif two:
                    if s[i + 1] in "0123456":
                        ways += dfs(i + 2)
            memo[i] = ways
            return memo[i]
        return dfs(0)

