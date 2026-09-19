class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        f = Counter(nums)
        for num, k in f.items():
            if k > n // 3:
                ans.append(num)
        return ans