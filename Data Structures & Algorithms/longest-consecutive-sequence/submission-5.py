class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        ans = 0
        for num in nums:
            if num - 1 not in seen:
                l = 0
                while num + l in seen:
                    l += 1
                ans = max(ans, l)
        return ans
                