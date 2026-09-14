class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        ans = float('inf')

        while l <= r:
            leastWeight = (l + r) // 2
            daysUsed = 1
            currWeight = 0
            for weight in weights:
                if currWeight + weight > leastWeight:
                    daysUsed += 1
                    currWeight = 0
                currWeight += weight
            if daysUsed > days:
                l = leastWeight + 1
            else:
                ans = min(ans, leastWeight)
                r = leastWeight - 1
        return ans