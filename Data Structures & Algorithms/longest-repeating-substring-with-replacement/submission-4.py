class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = {} # char : freq
        l = 0
        res = 0
        maxF = 0
        # ABAAAAAAAAABBBBB k = 2
        # (r - l + 1) - maxFreqCount < k
        for r in range(len(s)):
            freqs[s[r]] = 1 + freqs.get(s[r], 0)
            maxF = max(maxF, freqs[s[r]])
            if (r - l + 1) - maxF > k:
                freqs[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res




