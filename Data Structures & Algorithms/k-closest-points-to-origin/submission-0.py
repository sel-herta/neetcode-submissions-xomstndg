class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = []
        for x, y in points:
            dists.append((x**2 + y**2, [x, y]))
        print(dists)
        
        heapq.heapify_max(dists)
        while len(dists) > k:
            heapq.heappop_max(dists)
        ans = []
        for data in dists:
            ans.append(data[1])
        return ans