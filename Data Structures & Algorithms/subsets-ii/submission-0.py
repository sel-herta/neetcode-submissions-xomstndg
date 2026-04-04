class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        def dfs(i, curSub):
            if i >= len(nums):
                res.append(curSub.copy())
                return
            curSub.append(nums[i])
            dfs(i + 1, curSub)
            curSub.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, curSub)
        
        dfs(0, [])
        return res