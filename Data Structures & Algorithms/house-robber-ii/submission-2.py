class Solution:
    def rob(self, nums: List[int]) -> int:
        # subproblem
        # let dfs(i) be the maximum amount of profit when available houses are nums[0...i]
        # choices
        # 1) rob house
        # 2) skip house
        # recurrence relation = 
        # dfs(i) = max(dfs(i + 1), nums[i] + dfs(i + 2))
        memo = {}
        memo2 = {}
        nums1 = nums[1:len(nums)]
        nums2 = nums[:len(nums) - 1]

        if len(nums) == 1:
            return nums[0]
        
        def dfs(i):
            if i >= len(nums1):
                return 0
            if i == len(nums1) - 1:
                return nums1[i]
            if i in memo:
                return memo[i]
            rob = nums1[i] + dfs(i + 2)
            skip = dfs(i + 1)
            res = max(rob, skip)
            memo[i] = res
            return res
        
        def dfs2(i):
            if i >= len(nums1):
                return 0
            if i == len(nums1) - 1:
                return nums2[i]
            if i in memo2:
                return memo2[i]
            rob = nums2[i] + dfs2(i + 2)
            skip = dfs2(i + 1)
            res = max(rob, skip)
            memo2[i] = res
            return res
        
        r1 = dfs(0)
        r2 = dfs2(0)
        return max(r1, r2)