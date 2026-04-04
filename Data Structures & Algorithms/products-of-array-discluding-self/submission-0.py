class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        # [1, 2, 3]
        for i in range(len(nums)):
            a = 0
            b = False
            for j in range(len(nums)):
                if j != i:
                    if b == False:
                        b = True
                        a = nums[j]
                    else:
                        a *= nums[j]
            ans.append(a)
        return ans