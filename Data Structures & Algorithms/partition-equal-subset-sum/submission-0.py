class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return  False
        target = sum(nums) // 2
        n  = len(nums)
        memo = {}
        def dfs(i, target):
            if target == 0:
                return True
            if i >= n or target < 0:
                return False
            state = (i, target)
            if state in memo:
                return memo[state]
            res = dfs(i + 1, target) or dfs(i + 1, target - nums[i])
            memo[state] = res
            return res
        return dfs(0, target)