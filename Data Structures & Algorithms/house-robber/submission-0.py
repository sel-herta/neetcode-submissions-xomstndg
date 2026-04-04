class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]
            robHouse = nums[i] + dfs(i + 2)
            skipHouse = dfs(i + 1)
            res = max(robHouse, skipHouse)
            cache[i] = res
            return res
        return dfs(0)