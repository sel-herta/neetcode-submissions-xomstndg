class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = float('-inf')
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSum = max(maxSum, curSum)
        return maxSum