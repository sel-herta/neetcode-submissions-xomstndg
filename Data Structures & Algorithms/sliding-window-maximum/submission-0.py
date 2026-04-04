class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        l = 0
        if k > len(nums):
            return ans
        for r in range(k - 1, len(nums)):
            sub_arr = sorted(nums[l:r + 1]) # o(nlogn * n)
            largest = sub_arr[-1]
            ans.append(largest)
            l += 1
        return ans