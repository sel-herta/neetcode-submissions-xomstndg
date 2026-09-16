class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            lv, rv, mv = nums[l], nums[r], nums[m]
            if mv == target:
                return True
            if lv == rv == mv:
                l += 1
                r -= 1
                continue
            if lv <= mv:
                if lv <= target < rv:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if lv < target <= rv:
                    l = m + 1
                else:
                    r = m - 1
        return False
                        