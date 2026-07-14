class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1, 1
        ans = nums[0]
        for num in nums:
            tmp = curMax * num
            curMax = max(num, curMax * num, curMin * num)
            curMin = min(num, tmp, curMin * num)
            ans = max(ans, curMax)
        return ans