class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        # "Hello" "World"
        for s in strs:
            l = len(s)
            res += str(l) + "#" + s
        return res
        # 5#Hello5#World
        # list = []

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            numToRead = int(s[i:j])
            ans.append(s[j + 1:j + numToRead + 1])
            i = j + numToRead + 1
        return ans
            