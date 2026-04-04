class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = [0] * 26
        if len(s1) > len(s2):
            return False
        # abc
        # lecabee
        # s1_freq = [1,1,1 0...]
        for c in s1:
            s1_freq[ord(c) - ord('a')] += 1
        l, r = 0, len(s1) - 1
        while r < len(s2):
            s2_freq = [0] * 26
            for i in range(l, r + 1, 1):
                s2_freq[ord(s2[i]) - ord('a')] += 1
            if s1_freq == s2_freq:
                return True
            r += 1
            l += 1
        return False