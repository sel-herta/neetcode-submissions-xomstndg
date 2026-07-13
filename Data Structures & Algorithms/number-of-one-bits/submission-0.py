class Solution:
    def hammingWeight(self, n: int) -> int:
        ans  =  0
        for i in range(32):
            if (1 << i) & n != 0:
                ans += 1
        return ans