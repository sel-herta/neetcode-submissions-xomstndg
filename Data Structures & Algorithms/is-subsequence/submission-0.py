class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        check = 0
        for c in s:
            found = False
            for i in range(check, len(t)):
                if c == t[i]:
                    check = i + 1
                    found = True
                    break
            if not found:
                return False
        return True
