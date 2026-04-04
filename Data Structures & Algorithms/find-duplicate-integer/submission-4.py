class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[abs(abs(nums[i]) - 1)] < 0:
                return abs(nums[i])
            else:
                nums[abs(abs(nums[i]) - 1)] *= -1