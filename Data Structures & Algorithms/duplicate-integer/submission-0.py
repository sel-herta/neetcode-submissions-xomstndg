class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp_list = []
        for item in nums:
            if item in temp_list:
                return True
            temp_list.append(item)
        return False
