class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        currCombo = []
        res = []

        def dfs(i, currSum):
            if currSum == target:
                res.append(currCombo.copy())
                return
            if currSum > target or i >= len(candidates):
                return
            currCombo.append(candidates[i])
            dfs(i+1, currSum + candidates[i])
            currCombo.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, currSum)
        
        dfs(0, 0)
        return res