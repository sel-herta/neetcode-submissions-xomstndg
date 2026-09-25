class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        curSum = 0

        prefixes = defaultdict(int)
        prefixes[0] = 1

        for num in nums:
            curSum += num
            diff = curSum - k
            ans += prefixes[diff]
            prefixes[curSum] += 1
        
        return ans