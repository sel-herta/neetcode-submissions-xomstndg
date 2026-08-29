class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthestPos = nums[0]
        for i in range(len(nums)):
            if i > farthestPos:
                return False
            farthestPos = max(farthestPos, i + nums[i])
        return True