class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        # a + b + c = 0
        # [-1,0,1,2,-1,-4]
        # [-4, -1, -1, -1, 1, 2]
        for i, num in enumerate(nums):
            if i > 0 and nums[i - 1] == num:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                tSum = num + nums[l] + nums[r]
                if tSum == 0:
                    ans.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif tSum > 0:
                    r -= 1
                elif tSum < 0:
                    l += 1
        return ans
                
