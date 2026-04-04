class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # if cur_sum is >= target, then stop extending the list
        res = []
        currCombo = []
        curr_sum = 0

        def dfs(i):
            nonlocal curr_sum
            curr_sum = 0
            for num in currCombo:
                curr_sum += num
            if i >= len(nums):
                return
            if curr_sum == target:
                res.append(currCombo.copy())
                return
            if curr_sum > target:
                return
            currCombo.append(nums[i])
            dfs(i)
            currCombo.pop()
            dfs(i+1)
        
        dfs(0)
        return res