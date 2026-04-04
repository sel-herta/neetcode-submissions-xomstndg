class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans = -1

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                ans = m
                break
            if nums[m] >= nums[l]:
                if target >= nums[l] and target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                # m is part of right side
                if target <= nums[r] and target >= nums[m]:
                    l = m + 1
                else:
                    r = m - 1
        return ans

            