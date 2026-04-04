class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if sorted(s) == sorted(t):
        #    return True
        #return False
        #the order of the characters don't matter, so maybe we just need
        #the length of the OG string and the unique characters and compare those two
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT