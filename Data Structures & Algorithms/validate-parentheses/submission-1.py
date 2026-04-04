class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # "([])("
        open = ["(", "{", "["]
        close = [")", "}", "]"]
        for c in s:
            if c in open:
                stack.append(c)
            else:
                if not stack:
                    return False
                n = stack[-1]
                if open.index(n) == close.index(c):
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
            return True

