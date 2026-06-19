class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans = 0
        maxf = 0
        for num, f in freq.items():
            if f > maxf:
                ans = num
                maxf = f
        return ans