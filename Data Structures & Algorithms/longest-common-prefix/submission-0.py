class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        check = 0
        smallestLen = float('inf')
        for word in strs:
            smallestLen = min(smallestLen, len(word))
        ans = ""
        while check < smallestLen:
            char = strs[0][check]
            for word in strs:
                if word[check] == char:
                    continue
                else:
                    return ans
            ans += char
            check += 1
        return ans