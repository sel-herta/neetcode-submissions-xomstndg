class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = 10000
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[r] > nums[l]:
                # it's already sorted, check l
                ans = min(nums[l], ans)
                break
            # do binary search
            m = (l + r) // 2
            if nums[m] >= nums[l]:
                # this is part of the left sorted portion
                # so there can be lower nums after mid
                l = m + 1
            else:
                # part of right sorted portion
                # so there can lower nums before mid
                r = m - 1
            ans = min(nums[m], ans)
        return ans