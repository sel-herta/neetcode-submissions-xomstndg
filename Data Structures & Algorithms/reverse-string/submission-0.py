class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        while l < r:
            tempR = s[r]
            s[r] = s[l]
            s[l] = tempR
            l += 1
            r -= 1