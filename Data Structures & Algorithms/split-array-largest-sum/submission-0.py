class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        lower, higher = max(nums), sum(nums)
        ans = sum(nums)
        while lower <= higher:
            trySum = (lower + higher) // 2
            currSum = 0
            currArrays = 1
            for num in nums:
                if currSum + num > trySum:
                    currSum = num
                    currArrays += 1
                else:
                    currSum += num
            if currArrays <= k:
                ans = trySum
                higher = trySum - 1
            else:
                lower = trySum + 1
        return ans
