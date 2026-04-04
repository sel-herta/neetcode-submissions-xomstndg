class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []

        def dfs(perm):
            if len(perm) >= len(nums):
                perms.append(perm.copy())
                return
            for i in range(len(nums)):
                if nums[i] in perm:
                    continue
                perm.append(nums[i])
                dfs(perm)
                perm.pop()

        dfs([])
        return perms