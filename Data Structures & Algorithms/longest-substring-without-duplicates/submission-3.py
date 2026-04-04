class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        maxC = 1
        # "abca"
        if len(s) < 2:
            return 1 if len(s) > 0 else 0
        seen = set()
        while r < len(s):
            if s[r] in seen:
                seen.clear()
                l += 1
                r = l
            else:
                seen.add(s[l])
                seen.add(s[r])
                #counter += 1
            maxC = max(maxC, len(seen))
            r += 1
        return maxC