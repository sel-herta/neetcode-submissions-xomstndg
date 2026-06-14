class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        ans = []
        currCombo = []
        def dfs(i):
            if i == len(digits):
                if currCombo:
                    ans.append(''.join(currCombo.copy()))
                return
            for char in mapping[digits[i]]:
                currCombo.append(char)
                dfs(i+1)
                currCombo.pop()
        dfs(0)
        return ans