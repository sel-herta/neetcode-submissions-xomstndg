class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {} # num : appearances
        for n in nums:
            freqs[n] = 1 + freqs.get(n, 0)
        keys = sorted(freqs, key=freqs.get)
        keys = keys[::-1]
        ans = []
        for i in range(k):
            ans.append(keys[i])
        return ans
        