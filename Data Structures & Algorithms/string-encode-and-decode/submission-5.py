class Solution:

    def encode(self, strs: List[str]) -> str:
        # len of str, delimiter (#)
        # ["cat", "cats"]
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
        
        # 4#cats5#catss
    def decode(self, s: str) -> List[str]:
        ans, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            l = int(s[i:j])
            ans.append(s[j + 1: j + 1 + l])
            i = j + 1 + l
        return ans

