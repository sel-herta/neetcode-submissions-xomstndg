class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = []
        for v in nums:
            if v in n:
                return True
            n.append(v)
        return False