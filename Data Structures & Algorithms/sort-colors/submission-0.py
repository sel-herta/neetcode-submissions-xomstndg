class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = [0, 0, 0]
        for num in nums:
            freq[num] += 1
        currIndex = 0
        while freq[0] > 0:
            freq[0] -= 1
            nums[currIndex] = 0
            currIndex += 1
        while freq[1] > 0:
            freq[1] -= 1
            nums[currIndex] = 1
            currIndex += 1
        while freq[2] > 0:
            freq[2] -= 1
            nums[currIndex] = 2
            currIndex += 1