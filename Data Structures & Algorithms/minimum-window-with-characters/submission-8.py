class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ""
        window, shortest = [None, None], 1001
        hash_t = {} # char : freq
        hash_s = {}
        if t != "" and len(t) > len(s):
            return ans
        for i in range(len(t)):
            hash_t[t[i]] = 1 + hash_t.get(t[i], 0)
        # s: OUZODYXAZV, t: XYZ
        # we want to make it so l goes until it is no longer valid
        # of the substring found
        l = 0
        have = 0

        for r in range(len(s)):
            # update hash_s to include new char
            hash_s[s[r]] = 1 + hash_s.get(s[r], 0)
            if s[r] in hash_t and hash_s[s[r]] == hash_t[s[r]]:
                have += 1
            while have == len(hash_t):
                if r - l + 1 < shortest:
                    shortest = r - l + 1
                    window = [l, r + 1]
                hash_s[s[l]] -= 1
                if s[l] in hash_t and hash_s[s[l]] < hash_t[s[l]]:
                    have -= 1
                l += 1
        
        return s[window[0]:window[1]] if shortest != 1001 else ""
            