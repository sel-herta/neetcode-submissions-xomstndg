class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # brute force:
        # go through 1 to len(piles)
        # if work, then it is the min answer

        possible_ans = []
        ans = 0
        
        l, r = 1, max(piles)
        while l <= r:
            m = (l + r) // 2
            total = 0
            for pile in piles:
                total += math.ceil(pile/m)
            
            if total <= h:
                ans = m
                r = m - 1
            else:
                l = m + 1
        
        return ans
