class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = [0] * 26
        s2_freq = [0] * 26
        if len(s1) > len(s2):
            return False
        # aac
        # aabaaae
        # s1_freq = [1,1,1 0...]
        for i in range(len(s1)):
            s1_freq[ord(s1[i]) - ord('a')] += 1
            s2_freq[ord(s2[i]) - ord('a')] += 1
        matches = 0
        for i in range(26):
            if s1_freq[i] == s2_freq[i]:
                matches += 1
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            index = ord(s2[r]) - ord('a')
            l_index = ord(s2[l]) - ord('a')

            # if matches are the same before we add
            # to the s2_freq, decrease match
            if s2_freq[index] == s1_freq[index]:
                matches -= 1

            s2_freq[index] += 1
            if s2_freq[index] == s1_freq[index]:
                matches += 1

            # if matches are the same before we remove
            # to the s2_freq, dec match
            if s2_freq[l_index] == s1_freq[l_index]:
                matches -= 1

            s2_freq[l_index] -= 1
            if s2_freq[l_index] == s1_freq[l_index]:
                matches += 1
            l += 1
        return matches == 26

